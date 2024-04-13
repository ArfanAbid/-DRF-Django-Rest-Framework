const loginForm=document.getElementById('login-form');
const searchForm=document.getElementById('search-form');
const contentContainer=document.getElementById('content-container');
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
    
    fetch(loginEndpoint,options) // promise
    .then(response =>{
        return response.json();
    })
    .then(data =>{
        // console.log(data);
        handelAuthData(data,getProductList);

        // window.location.href="index.html";
    })
    .catch(error =>{
        console.log(error);
    });
});

function handelAuthData(data, callback) {
    
    localStorage.setItem('access',data.access);
    localStorage.setItem('refresh',data.refresh);

    if (callback){
        callback();
    }
}


function writeToContainer(data){
    if (contentContainer){
        contentContainer.innerHTML="<pre>" +  JSON.stringify(data) + "</pre>"
    }
}

function getFetchOptions(method,jsObj){
    return{
        method: method === null ? "GET" : method,
        headers:{
            "Content-Type":"application/json",
            "Authorization":`Bearer ${localStorage.getItem('access')}`
        },
        body:jsObj ? JSON.stringify(jsObj) : null
    }
}

function isTokenValid(jsondata) {
    // const token=localStorage.getItem('access');
    // const refresh=localStorage.getItem('refresh');
    // if (token && refresh){
    //     if (jsondata.refresh!==refresh){
    //         return false;
    //     }
    //     return true;
    // }
    // return false;

    if(jsondata.code && jsondata.code === "token_not_valid"){
        // run a refresh token fetch
        alert("Please Login Again");
        return false;
    }
    return true;

}
function validdataJWTToken() {
    //fetch
    const endpoint=`${baseEndpoint}/token/verify/`;
    const options={
        method:'POST',
        headers:{
            "Content-Type":"application/json",
        },
        body:JSON.stringify({
            "token":localStorage.getItem('access')
        })
    }
    fetch(endpoint,options)
    .then(response =>{
        return response.json();
    })
    .then(data =>{
        // refresh Token
        console.log(data);
        isTokenValid(data);
    })


};


function getProductList(){

    const endpoint =`${baseEndpoint}/products/`;
    const options=getFetchOptions();
    fetch(endpoint,options)
    .then(response =>{
        return response.json();
    })
    .then(data =>{
        const validData=isTokenValid(data);
        if(validData){
            writeToContainer(data);
        }
    });
};

validdataJWTToken()
// getProductList()


// *************** Search   ***********************

searchForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(searchForm);
    let data = Object.fromEntries(formData);
    let searchParams = new URLSearchParams(data);
    const endpoint = `${baseEndpoint}/products/search/?${searchParams}`;
    console.log(endpoint);
    const headers = {
        "Content-Type": "application/json",
    }

    const authToken = localStorage.getItem('access') 
    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`
    }
    const options = {
        method: "GET",
        headers: headers
    }
    
    fetch(endpoint, options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json()})
        .then(data => {
            const validData = isTokenValid(data)
        if (validData && contentContainer){
            contentContainer.innerHTML = ""
            if (data && data.hits) {
                let htmlStr  = ""
                for (let result of data.hits) {
                    htmlStr += "<li>"+ result.title + "</li>"
                }
                contentContainer.innerHTML = htmlStr
                if (data.hits.length === 0) {
                    contentContainer.innerHTML = "<p>No results found</p>"
                }
            } else {
                contentContainer.innerHTML = "<p>No results found</p>"
            }
        }
})
        .catch(error => {
            console.log(error);
        });
});
