<template>
    <div>
        <button v-on:click="onclickStart"> Start </button>
    </div>
</template>
<script>
export default {
      name:"StartPanel",
      props:["onclickStart"]
}

</script>
