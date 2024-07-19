import express from 'express'
import mongoose from 'mongoose'

const PORT = 5000
const DB_URL = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6'

const app = express()
app.use( express.static('homepage'))
app.get('/', (req, res)=>{
    res.send()
})

async function startApp(){
    try{
        await mongoose.connect(DB_URL)
        app.listen(PORT, ()=>{console.log('Server stared on port ' + PORT)})
    }catch(e){
        console.log(e)
    }
}

startApp()




// import { MongoClient } from "mongodb";

// const client = new MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')

// let keyworlds

// async function getKeyworlds(){
//     await client.connect()
//     const db = client.db('admin')
//     const coll = db.collection('serverList')
//     console.log("Подключение с сервером успешно установлено");
//     const count = await coll.countDocuments();
//     console.log(`В коллекции ${coll.namespace} ${count} документов`);
//     const results = await coll.distinct('servername')
//     console.log(results)
//     keyworlds = results
//     await client.close();
//     console.log("Подключение закрыто");
//     return keyworlds
// }
// getKeyworlds()
// console.log(keyworlds)