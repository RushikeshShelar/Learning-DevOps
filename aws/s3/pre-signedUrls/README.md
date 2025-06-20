# 🔐 AWS S3 Pre-signed URLs

This project demonstrates how to generate and use **pre-signed URLs** to securely interact with a private S3 bucket using the **AWS SDK v3** in Node.js.

Pre-signed URLs allow temporary, limited access to S3 objects without exposing credentials or making the bucket public.

---

## 📁 Features

- ✅ Generate **pre-signed GET URL** to access a private object
- ✅ Generate **pre-signed PUT URL** to upload an object
- ✅ List all objects in the S3 bucket
- ✅ Delete a specific object

---

## 🛠️ Setup

1. **Install dependencies**

```bash
npm install
```

2. **Create a `.env.local` file**

```env
AWS_REGION=<your-region>
AWS_ACCESS_KEY_ID=<your-access-key-id>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key>

AWS_S3_BUCKET_NAME=<your-bucket-name>
AWS_S3_BUCKET_OBJECT_KEY=<your-object-key>  # (e.g. squad.jpg)
```

3. **Run the script**

```bash
node index.js
```

Uncomment specific function calls inside `main()` in `index.js` to test:

```js
// await getObjectUrl(...)
// await putObjectUrl(...)
// await deleteObject(...)
// await listObjects()
```

---

## 📂 Project Structure

| File         | Purpose                                                  |
| ------------ | -------------------------------------------------------- |
| `index.js`   | Core logic for interacting with S3 using pre-signed URLs |
| `.env.local` | Environment variables for credentials and configuration  |

---

## 🔐 Notes

- The URLs generated are **temporary** (1 hour by default).
- Useful for securely allowing users to **download or upload files** without exposing S3 credentials or opening the bucket to public access.
- All actions use the AWS SDK v3 and are **console-tested**.

---

## 🧪 Examples

```js
// Generate a GET pre-signed URL
await getObjectUrl("folder/image.jpg");

// Generate a PUT pre-signed URL
await putObjectUrl("video.mp4", "video/mp4");

// List all objects in the bucket
await listObjects();

// Delete an object from the bucket
await deleteObject("uploads/put/video.mp4");
```

---

> This repo is part of Rushikesh Shelar’s AWS learning journey 🚀

