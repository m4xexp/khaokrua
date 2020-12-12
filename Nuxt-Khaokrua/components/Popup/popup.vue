<template>
  <div class="popup-container">
    <v-dialog
      v-model="dialog"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">
          Use Google's location service?
        </v-card-title>

        <v-card-text>
          Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    
  </div>
</template>

<script>
export default {
  name: 'popup',
}
</script>


<style lang="scss" scoped>

.card-popup {
  border-radius: 10px;
}

.title-popup span {
    margin: 30px;
    font-size: 30px;
    font-weight: bold;
}

.div-action{

    width: 60%;
    padding: 20px;
}
</style>