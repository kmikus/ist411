var JSONObject = 
	{"employees":
		[
			{"firstName": "John", "lastName": "Doe"},
			{"firstName": "Anna", "lastName": "Smith"},
			{"firstName": "Peter", "lastName": "Jones"}
		]
	};

var count=Object.keys(JSONObject.employees).length;
console.log(count);

for (var i=0; i<count; i++) {
	alert(JSONObject.employees[i].firstName + " " + JSONObject.employees[i].lastName);
}

$(document).ready(function() {
	JSONObject = {
		"name": "Kevin Mikus",
		"street": "9 Johndoe Ave",
		"age": "26",
		"phone": "215-215-2152"
	};
	$("#jname").html(JSONObject.name);
	$("#jage").html(JSONObject.age);
	$("#")
})