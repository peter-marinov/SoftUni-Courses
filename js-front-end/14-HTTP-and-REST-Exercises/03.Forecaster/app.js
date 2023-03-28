function attachEvents() {
    const CITIES_URL = 'http://localhost:3030/jsonstore/forecaster/locations/'
    const WEATHER_URL = 'http://localhost:3030/jsonstore/forecaster/today/'
    const FUTURE_WEATHER_URL = 'http://localhost:3030/jsonstore/forecaster/upcoming/'
    const forecastContainer = document.getElementById('forecast');
    const currentWeatherContainer = document.getElementById('current');
    const upcomingWeatherContainer = document.getElementById('upcoming');
    const locationInput = document.getElementById('location');
    const getBtn = document.getElementById('submit');

    const sunny = '&#x2600';
    const partlySunny = '&#x26C5';
    const overcast = '&#x2601';
    const rain = '&#x2614';
    const degrees = '&#176';

    getBtn.addEventListener('click', getWeatherHandler);

    async function getWeatherHandler() {
        

        const allCitiesRes = await fetch(CITIES_URL);
        const allCities = await allCitiesRes.json();
        
        for (const city of allCities) {
            const { code, name } = city;
            if ( name === locationInput.value) {
                currentWeatherContainer.innerHTML = '<div class="label">Current conditions</div>';
                upcomingWeatherContainer.innerHTML = '<div class="label">Three-day forecast</div>';
                forecastContainer.style.display = 'block';

                const cityWeatherRes = await fetch(`${WEATHER_URL}${code}`);
                const { forecast, name } = await cityWeatherRes.json();
                
                let weather = undefined;
                if (forecast.condition === 'Sunny') {
                    weather = sunny;
                } else if (forecast.condition === 'Partly sunny') {
                    weather = partlySunny;
                } else if (forecast.condition === 'Overcast') {
                    weather = overcast;
                } else {
                    weather = rain;
                }

                createElement('span', '', currentWeatherContainer, '', ['condition', 'symbol'], '', weather);
                const spanCurrentWeatherContainer = createElement('span', '', currentWeatherContainer, '', ['condition']);
                createElement('span', name, spanCurrentWeatherContainer, '', ['forecast-data']);
                createElement('span', '', spanCurrentWeatherContainer, '', ['forecast-data'], '', `${forecast.low}${degrees}/${forecast.high}${degrees}`);
                createElement('span', forecast.condition, spanCurrentWeatherContainer, '', ['forecast-data']);
                
                const upComingWeatherRes = await fetch(`${FUTURE_WEATHER_URL}${code}`);
                const upComingWeather = await upComingWeatherRes.json();
                const upcomingDivContainer = createElement('div', '', upcomingWeatherContainer, '', ['forecast-info']);
                console.log(upComingWeather)
                for (const day of upComingWeather.forecast) {
                    if (forecast.condition === 'Sunny') {
                        weather = sunny;
                    } else if (forecast.condition === 'Partly sunny') {
                        weather = partlySunny;
                    } else if (forecast.condition === 'Overcast') {
                        weather = overcast;
                    } else {
                        weather = rain;
                    }
                    const divContainer = createElement('span', '', upcomingDivContainer, '', ['upcoming']);
                    createElement('span', '', divContainer, '', ['symbol'], '', weather);
                    createElement('span', '', divContainer, '', ['forecast-data'], '', `${day.low}${degrees}/${day.high}${degrees}`);
                    createElement('span', day.condition, divContainer, '', ['forecast-data']);
                    


                }
            }
        }
    }

    function createElement(type, content, parentNode, id, classes, attributes, htmlInner) {
        const htmlElement = document.createElement(type);
    
        if (content && type !== 'input') {
            htmlElement.textContent = content;
        }
    
        if (content && type === 'input') {
            htmlElement.value = content;
        }
    
        if (id) {
            htmlElement.id = id;
        }
    
        // ['list', ]
        if (classes) {
            htmlElement.classList.add(...classes);
        }
    
    
        // { src: 'link'}
        if (attributes) {
            for (const key in attributes) {
                htmlElement.setAttribute(key, attributes[key])
            }
        }

        if (htmlInner) {
            htmlElement.innerHTML = htmlInner;
        }
    
        if(parentNode) {
            parentNode.appendChild(htmlElement);
        }
        
        return htmlElement;
    }
}

attachEvents();