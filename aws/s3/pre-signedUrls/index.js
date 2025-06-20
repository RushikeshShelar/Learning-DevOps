require("dotenv").config();

const { S3Client, GetObjectCommand, PutObjectCommand, ListObjectsCommand, DeleteObjectCommand } = require("@aws-sdk/client-s3");
const { getSignedUrl } = require("@aws-sdk/s3-request-presigner");


const s3Client = new S3Client({
    region: process.env.AWS_REGION || "ap-south-1",
    credentials: {
        accessKeyId: process.env.AWS_ACCESS_KEY_ID || "",
        secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY || ""
    }
});


// Function to get a pre-signed URL for an object in S3
/**
 * Generates a pre-signed URL for an object in S3.
 * @param {string} key - The key of the object in S3.
 * @returns {Promise<string>} - A promise that resolves to the pre-signed URL.
 */
async function getObjectUrl(key) {
    // Create a command to get the object from S3
    const command = new GetObjectCommand({
        Bucket: process.env.AWS_S3_BUCKET_NAME || "",
        Key: key
    });

    // Generate a signed URL for the command
    const signedURL = getSignedUrl(s3Client, command, { expiresIn: 3600 }); // URL valid for 1 hour
    return signedURL;
}


// Function to put an object in S3 (not implemented in this example)
/**
 * Puts an object in S3 and returns a pre-signed URL for it.
 * @param {string} filename - The filename of the object to put in S3.
 * @returns {Promise<string>} - A promise that resolves to the pre-signed URL.
 */
async function putObjectUrl(filename, contentType) {
    const command = new PutObjectCommand({
        Bucket: process.env.AWS_S3_BUCKET_NAME || "",
        Key: `uploads/put/${filename}`,
        ContentType: contentType
    });

    const signedURL = await getSignedUrl(s3Client, command, { expiresIn: 3600 }); // URL valid for 1 hour
    return signedURL;
}

// Function to Delete an object in S3
/**
 * Deletes an object from S3.
 * @param {string} key - The key of the object to delete.
 * @returns {Promise<void>} - A promise that resolves when the object is deleted.
 */
async function deleteObject(key) {
    const command = new DeleteObjectCommand({
        Bucket: process.env.AWS_S3_BUCKET_NAME || "",
        Key: key
    });
    await s3Client.send(command);
    console.log(`Object with key ${key} deleted successfully.`);
    return;
}


// Function to list objects in S3 
/**
 * 
 * @returns {Promise<Array>} - A promise that resolves to an array of objects in the S3 bucket.
 */
async function listObjects() {
    const command = new ListObjectsCommand({
        Bucket: process.env.AWS_S3_BUCKET_NAME || "",
        key: "/"
    });
    const result = await s3Client.send(command);
    return result.Contents.map(item => ({
        Key: item.Key,
        LastModified: item.LastModified,
        Size: item.Size
    }));
}

async function main() {
    // Uncomment the following lines to test getting a pre-signed URL for an object
    const key = process.env.AWS_S3_BUCKET_OBJECT_KEY || "squad.jpg";
    const url = await getObjectUrl(key);
    console.log("Signed URL:", url);

    // Uncomment the following lines to test uploading objects
    // console.log("UPLOAD VIDEO URL:", await putObjectUrl(`video-${Date.now()}.mp4`, "video/mp4"));
    // console.log("UPLOAD IMAGE URL:", await putObjectUrl(`image-${Date.now()}.jpg`, "image/jpeg"));

    // Uncomment the following lines to test deleting an object
    // const key = "uploads/put/image-1750435440374.jpeg";
    // await deleteObject(key);

    // Uncomment the following lines to test listing objects in the S3 bucket   
    // const objects = await listObjects();
    // console.log("Objects in S3 Bucket:", objects);
}

main();