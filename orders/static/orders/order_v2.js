document.addEventListener('DOMContentLoaded', () => {
    $('.addbutton').click(function(){            
        var meal = $(this).attr("data-meal");
        // Get data of pizza selection
        if (meal === "pizza") {
            var pizzaType = $(this).attr("data-pizzatype");
            var pizzaOption = $(this).attr("data-option");
            var size = $(this).attr("data-size");
            var price = $(this).attr("data-price");
            var toppings = [];
            console.log(pizzaType + " " + pizzaOption + " " + size + " $" + price);
            // Get selection of toppings or items
            if (pizzaType === "Regular"){
                if (pizzaOption === "0") {
                    var toppings = ["None"]
                } else if (pizzaOption === "1") {
                    var toppings = getOptions("Regular1")    
                } else if (pizzaOption === "2") {
                    var toppings = getOptions("Regular2")
                } else if (pizzaOption === "3") {
                    var toppings = getOptions("Regular3")
                } else if (pizzaOption === "5") {
                    var toppings = getOptions("Regular5")
                }
            } else if (pizzaType === "Sicilian") {
                if (pizzaOption === "0") {
                    var toppings = ["None"]
                } else if (pizzaOption === "1") {
                    var toppings = getOptions("Sicilian1")    
                } else if (pizzaOption === "2") {
                    var toppings = getOptions("Sicilian2")
                } else if (pizzaOption === "3") {
                    var toppings = getOptions("Sicilian3")
                } else if (pizzaOption === "5") {
                    var toppings = getOptions("Sicilian5")
                }
            }
            //console.log(toppings)
            // Send AJAX request with the order item
            var json_toppings = JSON.stringify(toppings);
            $.ajax({
                type:"GET",
                url: "/add",
                data:{
                    meal: meal,
                    pizza_type: pizzaType,
                    pizza_option: pizzaOption,
                    size: size,
                    price: price,
                    toppings: json_toppings
                },
                success: function(response) {
                    alert('AJAX successfull ' + response)
                }
            })
        // Get data of other meal types and send ajax request
        } else if (meal === "sub") {
            var subName = $(this).attr("data-sub");
            var size = $(this).attr("data-size");
            var price = $(this).attr("data-price");
            console.log(subName + " " + size + " " + "$" + price);
            $.ajax({
                type:"GET",
                url: "/add",
                data:{
                    meal: meal,
                    sub: subName,
                    size: size,
                    price: price,
                },
                success: function(response) {
                    alert('AJAX successfull ' + response)
                }
            })
        } else if (meal === "pasta") {
            var pasta = $(this).attr("data-pasta");
            var price = $(this).attr("data-price");
            console.log(pasta + " $" + price);
            $.ajax({
                type:"GET",
                url: "/add",
                data:{
                    meal: meal,
                    pasta: pasta,
                    price: price,
                },
                success: function(response) {
                    alert('AJAX successfull ' + response)
                }
            })
        } else if (meal === "salad") {
            var salad = $(this).attr("data-salad");
            var price = $(this).attr("data-price");
            console.log(salad + " $" + price);
            $.ajax({
                type:"GET",
                url: "/add",
                data:{
                    meal: meal,
                    salad: salad,
                    price: price,
                },
                success: function(response) {
                    alert('AJAX successfull ' + response)
                }
            })
        } else if (meal === "platter") {
            var platter = $(this).attr("data-platter");
            var size = $(this).attr("data-size");
            var price = $(this).attr("data-price");
            console.log(platter + " " + size + " $" + price);
            $.ajax({
                type:"GET",
                url: "/add",
                data:{
                    meal: meal,
                    platter: platter,
                    size: size,
                    price: price,
                },
                success: function(response) {
                    alert('AJAX successfull ' + response)
                }
            })
        }
    })
});

// Function to get toppings/items selection from the page
function getOptions(option_id) {
    var selected = []
    console.log("Pizza option recognized")
    var td = document.getElementById(option_id);
    //console.log(td);
    var selections =  td.getElementsByTagName("select");
    for (const s of selections) {
        var topping = s.options[s.selectedIndex].value;
        //console.log(topping);
        selected.push(topping);
    };
    //console.log(selected)
    return selected;  
}