const upload_button = document.getElementById('btn_image');
const image = document.getElementById('image');
const file = document.getElementById('file');

upload_button.addEventListener('click',function(){
    file.click();
})


file.addEventListener('change',function(){
    const chosenFile = this.files[0]
    console.log(chosenFile)
    if (chosenFile) {
        const reader = new FileReader();
        reader.addEventListener('load',function(){
            image.setAttribute('src',reader.result)
        });
        reader.readAsDataURL(chosenFile)   
    }
})


// ================================== HANDLE LIKE BUTTONS========================================

const comment_filed = document.querySelectorAll('#exampleFormControlInput1')

comment_filed.forEach((textbox)=>{
    textbox.addEventListener('keyup',(e)=>{
        if(e.keyCode != 13 && textbox.value === "") {
            return;
        }else{
        const text = e.target.value;
        console.log("you press the enter key")
        }
    })
})
















