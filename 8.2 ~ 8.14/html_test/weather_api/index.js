async function getApi(city){
    const API_KEY = ''
    const API_URL = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${API_KEY}`
    const response = await fetch(API_URL);
    const json = await response.json();
    
    // console.log(json)

    return json;

}

function setImage(main) {
    const image = document.querySelector('.weather-box img');
    // switch(main){
    // case "Clear" :
    //     image.src = "images/clear.png";
    //     break;
    // case "Rain":
    //     image.src = 'images/rain.png';
    //     break;
    // case "Snow":
    //     image.src = "images/snow.png";
    //     break;
    // case "Clouds":
    //     image.src = 'images/cloud.png';
    //     break;
    // case 'Haze':
    //     image.src = 'images/mist.png';
    //     break;
    // default:
    //     image.src = '';
    // }
        // 더 효율적으로 리팩토링
    const images = {
        'Clear' : "images/clear.png",
        'Rain' : 'images/rain.png',
        'Snow' : 'images/snow.png',
        'Clouds' : 'images/cloud.png',
        'Haze' : 'images/mist.png',
    }
    // key 값을 동적으로 불러온다.
    if (images[main]){
        image.src = images[main];
    }
    else{
        image.src = '';
    }
    
}
// document 안의 실제 HTML 요소에 접근
const container = document.querySelector('.container');
const search = document.querySelector('.search-box button');
const weatherBox = document.querySelector('.weather-box');
const weatherDetails = document.querySelector('.weather-details');
const error404 = document.querySelector('.not-found');

// 이벤트 리스너를 달아준다.
// 함수를 바깥에 선언해도 되고, 직접 안에 이름없는 함수를 넣어도 된다.
search.addEventListener('click', async () => {
    // 사용자의 입력값을 받는 태그들(input, textarea)
    // value라는 속성을 가집니다.
    // value = 사용자의 입력값을 가져옵니다.
    const city = document.querySelector('.search-box input').value;
    console.log(city);

    // 변수명만 if문에다가 적을 경우
    // city > city !== null && city !== ""
    // !city > city === null || city === ""
    if (!city){
        return;
    }

    // try ~ catch : try 안에 구문을 실행하는 동안 에러가 났을때 처리하기 위해 쓰는 문법이다.

    const json = await getApi(city);
    console.log(json);
    // api 값이 404 not found 일 때 유효한 주소를 찾지 못했다고 띄움
    if (json.cod === '404') {
        container.style.height = "400px";
        weatherBox.style.display = "none";
        weatherDetails.style.display = 'none';
        error404.style.display = 'block';
        error404.classList.add("fadeIn");
        return;
    }

    error404.style.display = 'none';
    error404.classList.remove('fadeIn');

    
    const temperature = document.querySelector('.weather-box .temperature');
    const description = document.querySelector('.weather-box .description');
    const humidity = document.querySelector('.weather-details .humidity span');
    const wind = document.querySelector(".weather-details .wind span");

    console.log(json.weather[0].main);

    setImage(json.weather[0].main);
    
    // parseInt = string => int로 바꿔줌
    temperature.innerHTML = `${parseInt(json.main.temp)}<span>°C</span>`;
    description.textContent = `${json.weather[0].description}`;
    humidity.textContent = `${json.main.humidity}%`;
    wind.textContent = `${parseInt(json.wind.speed)}Km/h`;

    weatherBox.style.display = '';
    weatherDetails.style.display = '';
    weatherBox.classList.add("fadeIn");
    weatherDetails.classList.add("fadeIn");
    container.style.height = '590px';
});