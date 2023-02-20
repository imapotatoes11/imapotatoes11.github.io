import './App.css'

import { useEffect, useState } from 'react'
//
export default function App() {
  
  //WEATHER I WANT TO DIE

  let weatherIcons = {1000: ['moon.svg', 'sun.svg'], 1003: 'cloud-sun.svg', 1006: 'cloud.svg', 1009: 'cloud.svg', 1030: 'cloud-fog.svg', 1135: 'cloud-fog.svg', 1147: 'cloud-fog.svg', 1063: 'cloud-drizzle.svg', 1150: 'cloud-drizzle.svg', 1153: 'cloud-drizzle.svg', 1168: 'cloud-drizzle.svg', 1198: 'cloud-drizzle.svg', 1240: 'cloud-drizzle.svg', 1249: 'cloud-snow.svg', 1066: 'cloud-snow.svg', 1114: 'cloud-snow.svg', 1117: 'cloud-snow.svg', 1207: 'cloud-snow.svg', 1210: 'cloud-snow.svg', 1213: 'cloud-snow.svg', 1216: 'cloud-snow.svg', 1219: 'cloud-snow.svg', 1222: 'cloud-snow.svg', 1252: 'cloud-snow.svg', 1255: 'cloud-snow.svg', 1258: 'cloud-snow.svg', 1072: 'cloud-hail.svg', 1069: 'cloud-hail.svg', 1171: 'cloud-hail.svg', 1201: 'cloud-hail.svg', 1204: 'cloud-hail.svg', 1237: 'cloud-hail.svg', 1261: 'cloud-hail.svg', 1264: 'cloud-hail.svg', 1087: 'cloud-lightning.svg', 1273: 'cloud-lightning.svg', 1276: 'cloud-lightning.svg', 1279: 'cloud-lightning.svg', 1282: 'cloud-lightning.svg', 1180: 'cloud-rain.svg', 1183: 'cloud-rain.svg', 1186: 'cloud-rain.svg', 1189: 'cloud-rain.svg', 1243: 'cloud-rain.svg', 1192: 'cloud-rain-wind.svg', 1195: 'cloud-rain-wind.svg', 1246: 'cloud-rain-wind.svg'}

  const [data, setData] = useState(null);

  useEffect(() => {
    const getWeather = async () => {
      const res = await fetch('https://api.weatherapi.com/v1/current.json?key=2251d57253504ce190315553231801&q=M2J3J8&aqi=no')
      let resJson = await res.json()
      setData(resJson)
    }
    getWeather()
  }, []);
  
  //WEATHER I WANT TO DIE
  
  const monthArr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  const [time, setTime] = useState(null)
  let date = new Date()
  let day = 'DAY ' + (date.getDate() % 2 == 0 ? 2 : 1 )
  let weekday = date.getDay()
  let month = monthArr[date.getMonth()]
  const dateNum = date.getDate()

  let temperature = data != null ? Math.round(data['current']['feelslike_c']) + '°C' : ''
  let weatherImg = data != null ? data['current']['condition']['code'] == 1000 ? weatherIcons[data['current']['condition']['code']][data['current']['is_day']] : weatherIcons[data['current']['condition']['code']] : 'cloud-off.svg'
  let weatherForcast = data != null ? data['current']['condition']['text'] : 'Fetching Data'
  
  useEffect(() => {

    setInterval(() => {
      
      setTime(timer())
      
    }, 1000)

  }, [])

  function search(event) {
    if (event.key == 'Enter') {
      console.log(4)
      let searchTerm = document.getElementById('searchBar').value 
      window.location.href='https://duckduckgo.com/' + searchTerm
    }
  }

  return (
    <div id='div'>
      <div id='left'>
        <p id='time'>{time}</p>
        <p id='day'>{weekday == 0 || weekday == 6 ? 'No School' : day}</p>
        <div id='search'>
          <input onKeyPress={(e) => search(e)} id='searchBar' type='text' placeholder='Search'></input>
        </div>
        <div id='buttons--row1'>
          {button('https://mail.google.com/mail/u/0/#inbox', 'mail.svg')}
          {button('https://docs.google.com/document/u/0/', 'file.svg')}
          {button('https://www.notion.so/', 'list-checks.svg')}
        </div>
        <div id='buttons--row2'>
          {button('https://classroom.google.com/u/0/h', 'contact.svg')}
          {button('https://tdsb.elearningontario.ca/d2l/login?sessionExpired=0&target=%2fd2l%2fhome', 'backpack.svg')}
          {button('https://ide.geeksforgeeks.org/1a8a5f6c-8f39-4e6a-aa57-db41fde311ec', 'code-2.svg')}
          
        </div>
      </div>  
      <hr></hr>
      <div id='right'>
        <p id='dateText'>{month} {dateNum}</p>
        <div id='weather'>
          <div id='weather-imgTemp'>
            <img id='weatherImg' src={weatherImg}></img>
            <p id='weatherTemp'>{temperature}</p>
          </div>
          <p id='weatherForcast'>{weatherForcast}</p>
        </div>
        <div id='moreLinks'>
          <img src='coffee.svg'></img><br></br>
          <div id='idkNameAnymore'>
          <p onClick={() => {window.location.href='https://discord.com/app'}} id='moreLinks--link'>Discord</p>
          <p id='moreLinks--link' onClick={() => {window.location.href='https://chess.com'}}>Chess.com</p>
          <p id='moreLinks--link' onClick={() => {window.location.href='https://mcpt.ca'}}>MCPT</p>
          </div>
        </div>
      </div>
    </div>
  )
}

function timer() {
  const dateObject = new Date()
  let hour = dateObject.getHours()
  let minute = dateObject.getMinutes()
  let trail = ' AM'
  if (String(minute).length == 1) {
    minute = '0' + String(minute)
  }
  if (hour > 12) {
    hour = hour % 12
    trail = ' PM'
  }
  const currentTime = hour + ':' + minute + trail
  return currentTime
}

function button(link, image) {
  return <button id='button' onClick={() => {window.location.href=link}}><img src={image}></img></button>
}

