/**
 * Get all dealerships
 */

 const Cloudant = require('@cloudant/cloudant');


 async function main(params) {
     const cloudant = Cloudant({
         url: params.COUCH_URL,
         plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } }
     });
 
 
     try {
         let dbList = await cloudant.db.use('dealerships');
         return { "dbs": dbList };
     } catch (error) {
         return { error: error.description };
     }
 
 }
