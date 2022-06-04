
function sendtoAWS () {
    var msgI=document.getElementById('msg').value;
    //console.log(msgI);
    let currentDate = new Date()
    let time = currentDate.getHours() + ":" + currentDate.getMinutes() + ":" + currentDate.getSeconds();
    //console.log(time);
    var msgJson={
        'name': time,
        "message": msgI
    }
    let config = {
        headers: {
          "Content-Type": "application/json",
          'Access-Control-Allow-Origin': '*',
          "Access-Control-Allow-Headers": "Content-Type"
          
        },
        proxy: {
            host: '127.0.0.1',
            port: 3000
            }
    }

    console.log(msgJson);
    var awsPostPath='https://0c0elmusa2.execute-api.us-east-1.amazonaws.com/Prod/senddata/sqs'
    axios.post(awsPostPath,msgJson,config).then(
        (response) => {
            console.log(response);
        },
        (error)=> {
            console.log(error);
        }
    );

}