animals = [['Sei whale', 'Blue whale', 'North atlantic right whale', 'North pacific right whale', 'Wolverine', 'Vancouver island marmot', 'Fin whale', 'Wood bison', 'Sea otter', 'Haida ermine', 'Whooping crane', 'Eskimo curlew', 'Sprague\'s pipit', 'Marbled murrelet', 'Short tailed albatross', 'Pink-footed shearwater', 'Spotted turtle', 'Blue racer', 'Leatherback sea turtle', 'Blanding\'s turtle', 'Oregon spotted frog', 'Atlantic whitefish', 'Shortnose cisco', 'Copper redhorse', 'Atlantic salmon', 'Northern wolffish', 'Lake lamprey', 'Rusty patched bumblebee', 'Hungerford\'s crawling water beetle', 'Northern barrens tiger beetle', 'Mottled duskywing', 'Hine\'s emerald', 'Dakota skipper', 'Poweshiek skipperling', 'Tubercled blossom', 'Snuffbox mussel', 'Pinto abalone', 'Round hickorynut', 'Banff springs snail', 'Salamander mussel', 'Rayed bean'],
['Caribou', 'Gray bat', 'Hawaiian hoary bat', 'North Atlantic right whale', 'Sei whale', 'Whooping crane', 'Atlantic bluefin tuna', 'Loggerhead sea turtle', 'Red wolf', 'California condor', 'Bog turtle', 'American burying beetle', 'Alabama beach mouse', 'Amargosa vole', 'Black-footed ferret', 'Anastasia island mouse', 'Florida bonneted bat', 'Florida panther', 'Florida salt marsh vole', 'Florida man', 'Fresno kangaroo rat', 'Giant kangaroo rat', 'Gray bat', 'Gulf Coast jaguarundi', 'Key deer', 'Key largo cotton mouse', 'Key largo wooden rat']]

countries = ["Canada", "United States of America"]


function dowiki(place) {
        var URL = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=';

        URL += "&titles=" + place;
        URL += "&rvprop=content";
        URL += "&callback=?";
        $.getJSON(URL, function (data) {
            var obj = data.query.pages;
            var ob = Object.keys(obj)[0];
            try{
                document.getElementById('text').textContent = obj[ob]["extract"];
            }
            catch (err) {
                document.getElementById('text').innerHTML = "FAILED TO CONNECT TO WIKIPEDIA";
            }

        });
    }


function getCountry(country) {
    
  document.getElementById("text").innerHTML = ""
  document.getElementById("title").innerHTML = ""
  document.getElementById("titleTwo").innerHTML = ""

  let countryNum = 3
  for (let i = 0; i < countries.length; i++) {
    if (countries[i] == country) {
      countryNum = i
    }
  }
    if (countryNum == 3) {
    document.getElementById("text").innerHTML = "Uh oh, we haven't added support for this country yet <br> Please go click another country" 
  } else {
    let animal = Math.floor((Math.random() * animals[countryNum].length))
    document.getElementById("titleTwo").innerHTML = animals[countryNum][animal]
    dowiki(animals[countryNum][animal])
  }
  document.getElementById("title").innerHTML = "Showing For: " + country    
}

function getAnimal(animal) {

  document.getElementById("text").innerHTML = ""
  document.getElementById("title").innerHTML = ""
  document.getElementById("titleTwo").innerHTML = ""
  let hmm = 0
  for (let i = 0; i < animals.length; i++) {
    for (let j = 0; j < animals[i].length; j++) {
    
        if (animals[i][j] == animal) {
        
            hmm = 2
        
        }   
    }
  }
  if (hmm == 2) {
      document.getElementById("title").innerHTML = "Showing Animal: " + animal
      dowiki(animal)
  } else {
      document.getElementById("title").innerHTML = "Showing Animal: " + animal
      document.getElementById("text").innerHTML = "Sorry, either that is not a real animal or we haven't added support for it or it isn't an endangered animal. Please search for a different animal"
  
  }  
}

function getInfo(object, country) {

  if (country == 1) {

    getCountry(object)

  } else if (country == 0) {
  
    let x = 0
    for (let i = 0; i < countries.length; i++) {
        if (countries[i] == country) {
            x = 1
    }
    if (x == 1) {
        getCountry(object)
    } else {
        getAnimal(object)
    }
  }
  
  }

}
