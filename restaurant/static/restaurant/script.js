function reviewEdit() {
    currentRating = document.getElementsByName("reviewRating")[0].content;
    currentContent = document.getElementsByName("reviewContent")[0].content;
    currentDate = document.getElementsByName("reviewDate")[0].content;
    
    
    ratingelement = document.getElementById("id_rating");
    outputelement = document.createElement("output");
    contentelement = document.getElementById("id_content");

    ratingelement.parentNode.appendChild(outputelement);

    ratingelement.type = "range";
    ratingelement.min = 0;
    ratingelement.max = 10;
    ratingelement.oninput = function () {
        ratingelement.nextElementSibling.value = ratingelement.value+" / 10";
    }

    if(currentDate != "") {
        ratingelement.value = currentRating;
        outputelement.innerHTML = currentRating+" / 10";
        contentelement.innerHTML = currentContent;
        document.getElementById("form_submit").value = "Save";
        document.getElementById("form_method").value = "put";

        lastmod = document.createElement("span");
        lastmod.innerHTML = "(created on "+currentDate+")";
        lastmod.setAttribute("class", "edit-lastmod");
        ratingelement.parentNode.parentNode.appendChild(lastmod);
    } else {
        ratingelement.value = "10";
        outputelement.innerHTML = "10 / 10";
    }

    ratingelement.previousElementSibling.style.display = "none";

    contentelement.placeholder = "Enter your review here...";
    contentelement.previousElementSibling.style.display = "none";
}


function deleteMenuItem(element, redirect) {
    id = element.getAttribute("data-id");
    itemname = element.getAttribute("data-name");
    csrftoken = element.getAttribute("data-csrftoken");
    
    if(confirm('are you sure you want to delete "'+itemname+'"?')) {
        fetch('/api/menu-item/'+id, {
            headers: {
                "X-CSRFToken": csrftoken,
                "Content-Type": "application/json"
            },
            method: 'DELETE'
        })
        .then((resonse) => {
            alert(itemname+"successfully deleted!");
        })
        .catch((err) => {
            alert("error occurred: " + err.message);
        });
        
        if(redirect != '') {
            console.log(document.referrer);
            window.location.replace(redirect);
        }
        else {
            element = document.getElementById("menuitem-"+id);
            element.remove();
        }
        
    }
}

function toggleEditMenuItem(element) {
    if(element.getAttribute("data-editing") == "true") {
       document.getElementById("menuitem-"+id).style.display = "block";
        document.getElementById("menuitem-edit-"+id).style.display = "none";
        return;
    }

    next = element.nextElementSibling;
    id = next.getAttribute("data-id");
    itemname = next.getAttribute("data-name");
    inventory = next.getAttribute("data-inventory");
    photo = next.getAttribute("data-photo");
    price = next.getAttribute("data-price");
    csrftoken = next.getAttribute("data-csrftoken");

    document.getElementById("menuitem-"+id).style.display = "none";
    document.getElementById("menuitem-edit-"+id).style.display = "block";
}

function editMenuItem(form) {
   // form = element.parentNode;
    //token = element.getAttribute("data-csrftoken");
    const formData = new FormData(form);
    

    for(let [k,v] of formData) {
        console.log(k+" "+v);
    }

    fetch('/api/menu-item/'+id, {
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/json"
        },
        method: 'PUT',
        body: formData
    });
    console.log(responses);
}