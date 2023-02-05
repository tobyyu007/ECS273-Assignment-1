<template>
  <div style="height: 400px">
    <Bar 
      :data="jsonData"
      :options="chartOptions"
    />
  </div>
</template>


<script lang="ts">
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import axios from 'axios';
import { server } from '../helper';
import { ref, onMounted } from 'vue'
import ChartDataLabels from 'chartjs-plugin-datalabels';
import chartTrendline from 'chartjs-plugin-trendline';


// https://stackoverflow.com/questions/63279050/chart-js-not-dispalying-data-array-that-comes-from-an-axios-request

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ChartDataLabels, chartTrendline);
ChartJS.defaults.set('plugins.datalabels', {
  color: '#3A3226'
});

export default {
  name: 'BarChart',
  components: { Bar },
  data() {
    return {
      jsonData: {
        labels: [],
        datasets: [
          {
            data: [],
            backgroundColor: '#E87A90',
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
              display: false
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
        datasets: [
          {
            data: yearCount,
            backgroundColor: '#E87A90',
          }
        ],
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
          keys.unshift(keys[4])
          keys.splice(5, 7)
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