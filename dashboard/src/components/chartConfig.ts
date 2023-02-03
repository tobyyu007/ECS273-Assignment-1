import axios from 'axios';
import { server } from '../helper';


function fetchData(){
  var result = []
  axios.post(`${server}/fetchExample`)
    .then(resp => {
        var journalsData = resp.data.journals;
        //console.log(journalsData);
        var journals = Object.keys(journalsData);
        var journalsIndex = 0;
        var journalNames = [];
        var journalCount = []
        Object.keys(journalsData).forEach(function(journal) {
          journalNames.push(journal);
          journalCount.push(journalsData[journal]);
        });
        var test1 = ["123", "1444"]
        //console.log(journalNames.slice(0, 2));
        this.result = test1
    })
    .catch(error => console.log(error));
  return result
}

function getRandomInt() {
  return Math.floor(Math.random() * (50 - 5 + 1)) + 5
}

export function test(){
  var data = fetchData();
  console.log(data);
}

export const getData = () => ({
  labels: ['Jan'],
  datasets: [
    {
      label: 'Data One',
      backgroundColor: '#f87979',
      data: [
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt()
      ]
    }
  ]
})


/*
function getRandomInt() {
  return Math.floor(Math.random() * (50 - 5 + 1)) + 5
}

export const getData = () => ({
  labels: [
    'January' + getRandomInt(),
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
  ],
  datasets: [
    {
      label: 'Data One',
      backgroundColor: '#f87979',
      data: [
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt(),
        getRandomInt()
      ]
    }
  ]
})

export const options = {
  responsive: true,
  maintainAspectRatio: false
}
*/