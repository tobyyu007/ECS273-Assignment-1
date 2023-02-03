<template>
  <Bar 
    :data="jsonData"
  />
</template>


<script lang="ts">
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import axios from 'axios';
import { server } from '../helper';
import { ref, onMounted } from 'vue'

// https://stackoverflow.com/questions/63279050/chart-js-not-dispalying-data-array-that-comes-from-an-axios-request

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data() {
    return {
      jsonData: {
        labels: [],
        datasets: [{data: []}]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            title: {
              display: true,
              text: 'Custom Chart Title'
            }
        }
      }
    }
  },
  mounted(){
    this.loadData()
  },

  methods:
  {
    updateChart(years, yearCount){
      //console.log(this.jsonData)
      this.jsonData = {
        labels: years,
        datasets: [{data: yearCount}]
      }
      console.log(this.jsonData)
    },

    async loadData() {
      await axios.post(`${server}/fetchExample`)
      .then(resp => {
          var publishTimeData = resp.data.publishTime;
          //console.log(publishTimeData);
          var publishTimes = Object.keys(publishTimeData);
          var publishTimeDataIndex = 0;
          var years = [];
          var yearCount = []
          var keys = Object.keys(publishTimeData)
          keys.unshift(keys[25])
          keys.splice(26, 27)
          keys.push("Unknown")
          for (var key of keys){
            years.push(key)
            yearCount.push(publishTimeData[key])
          }
          this.updateChart(years, yearCount)
          //console.log(years);
          //console.log(yearCount);
          return true;
      })
      .catch(error => console.log(error));
    }
  },
}
</script>