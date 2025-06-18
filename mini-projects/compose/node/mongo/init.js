db = db.getSiblingDB('devops');
db.createCollection('test');
db.test.insert({ status: 'mongo is working 🎉' });