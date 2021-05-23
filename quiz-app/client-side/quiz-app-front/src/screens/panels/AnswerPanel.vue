<template>
     <div>
        <h4 class="classname"> Question No :{{quizNo}} </h4>
        <p> Answer {{quizAnswer}}</p>
        <p> {{quizContent}}</p>
        <button v-for="x in quizOptions" :key="x" disabled >{{x}}</button>
        <button> Next </button>
    </div>
</template>
<script>
    export default{
     name:"AnswerPanel",
     props:["quizNo","quizContent","quizOptions","quizAnswer","userClickedAnswer","result"]
    }
</script>
<style>
     p{
         color:red;
     }
     .classname
     {
         color:blue;
     }
     .correct-answer
     {
         background-color: green;
     }
     .wrong-answer
     {
         background-color: red;
     }

</style>