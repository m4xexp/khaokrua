<template>
  <div class="error-container">
    <v-sheet class="error-sheet">
      <div class="content">
        <h1>404</h1>
        <h4>ไม่นะ ไม่มีหน้าที่คุณต้องการเลย</h4>
        <p>
          ไม่พบหน้าที่คุณต้องการ
          บางทีอาจจะถูกลบหรือเปลี่ยนที่อยู่ใหม่แล้ว
        </p>
        <NuxtLink to="/"> <span>กลับไปยังหน้าแรก</span></NuxtLink>
      </div>
    </v-sheet>
  </div>
</template>

<script>
export default {}
</script>


<style lang="scss" scoped>
.error-sheet {
  position: absolute;
  display: block;
  top: 10%;
  left: 17%;
  right: 17%;
  bottom: 50%;
  align-items: center;
  background-color: white;
}

.error-sheet .content{
    text-align: center;
}

.content h1{
    font-size: 18vw;
    line-height: 1em;
}

.content h4{
    font-size: 2em;
    margin-bottom: 30px;
}
</style>
