<template>
  <div>
    <button type="button" class="btn btn-primary">{{ msg }}</button>
<!--    <p>{{ msg }}</p>-->
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "Ping",
  data() {
    return {
      msg: ''
    }
  },
  methods:{
    getMessage(){
      const path = 'http://127.0.0.1:5000/api/ping'
      axios.get(path)
        .then((response)=>{
        this.msg = response.data;
        })
        .catch((error)=>{
          console.error(error);
        })
    }
  },
  created() {
    this.getMessage()
  }

}
</script>

<style scoped>

</style>
