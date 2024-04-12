const loginForm=document.getElementById('login-form');
const baseEndpoint="http://localhost:8000/api";

loginForm.addEventListener('submit', (e) => {
    console.log(e);
    e.preventDefault();
    const loginEndpoint=`${baseEndpoint}/token/`;
    const loginFormData=new FormData(loginForm);
    let loginObjectData=Object.fromEntries(loginFormData);
    // console.log(loginObjectData);
    const options={
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(loginObjectData)
    };
    
    fetch(loginEndpoint,options)
    .then(response =>{
        console.log(response);
        return response.json();
    })
    .then(data =>{
        console.log(data);
        // localStorage.setItem('token',data.token);
        // window.location.href="index.html";
    })
    .catch(error =>{
        console.log(error);
    });
});