<template>
  <Line 
    :data="jsonData"
  />
</template>


<script lang="ts">
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'
import axios from 'axios';
import { server } from '../helper';
import { ref, onMounted } from 'vue'

// https://stackoverflow.com/questions/63279050/chart-js-not-dispalying-data-array-that-comes-from-an-axios-request

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

export default {
  name: 'App',
  components: { Line },
  data() {
    return {
      jsonData: {
        labels: [],
        datasets:[{data: []}]
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
        datasets:[{data: yearCount}]
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
          console.log(keys)
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