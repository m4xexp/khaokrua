<template>
    <v-dialog persistent v-model="$store.getters.getDialogState" width="500">
      <v-card>
        <v-card-title class="warning mb-6"> Alert </v-card-title>
        <v-card-text class="textDetail">
          {{ $store.getters.getDialogMsg }}
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="$store.dispatch({ type: 'dialogPopup', value: false, msg: '' })"
          >
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
export default {
  name: "PopUpDialog"
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Kanit:wght@200&display=swap');


* {
  list-style: none;
  outline: none;
  font-family: 'Kanit', sans-serif;
  box-sizing: border-box;
}

.textDetail{
  font-size: 30px;
}
</style>
