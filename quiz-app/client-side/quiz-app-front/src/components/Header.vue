<template>
    <div>
        <h1> {{title}} </h1>
    </div>
</template>
<script>
import { defineComponent } from '@vue/composition-api'

export default {
name : "Header",
props: ["title"]
}
</script>
