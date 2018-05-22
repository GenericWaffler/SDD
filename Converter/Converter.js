// JavaScript Document
function calculate() {
  var amount = parseFloat(document.getElementById("amount").value);
  var selection = document.getElementById("selection");
  var selecttwo = document.getElementById("selecttwo");
  var result = document.getElementById("result");
var rates = {
    USD : {
        USD: 1,
        EUR: 0.81,
        AUD: 1.3,
    },
    EUR : {
        EUR : 1,
        USD : 1.23,
        AUD : 1.6,
    },
	AUD : {
        AUD : 1,
        EUR : 0.63,
        USD : 0.77,
    },
	CM : {
		CM : 1,
        INCH : 0.394,
		KM : 0.00001,
		MILE : 0.000006214,
    },
	INCH : {
		INCH : 1,
        CM : 2.54,
		KM : 0.0000254,
		MILE: 0.00001578,
    },
	KM : {
		KM : 1,
        INCH : 39370.1,
		CM : 100000,
		MILE : 0.6214,
},
	MILE : {
		MILE : 1,
        INCH : 63360,
		KM : 1.609,
		CM : 160934,
},
};

if ( rates[selection.value] && rates[selection.value] [selecttwo.value] )
{
    result.value = amount * rates[selection.value][selecttwo.value];
}
else {
	result.value = "N/A";
}
}
