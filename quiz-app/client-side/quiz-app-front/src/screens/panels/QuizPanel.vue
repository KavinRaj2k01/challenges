<template>
    <div>
        <h4 > Question No :{{quizNo}}</h4>
        <p> {{quizContent}} </p>
        <div class='answer-container'><button class="answer-button" v-for="x in quizOptions" :key="x" v-on:click="onclick" :value="x"> {{x}} </button></div>
    </div>
</template>
<script>
export default{
    name:"QuizPanel",
    props:["quizNo","quizContent","quizOptions","quizAnswer","onQuizAnswer"],
    methods:{onclick:function(event)
    {
      if(event.target.value===this.quizAnswer)
      {
        this.onQuizAnswer(true,event.target.value);
      }
      else{
        this.onQuizAnswer(false,event.target.value);
      }
    }}
}
</script>

<style>
.answer-container
{
display:flex;  
flex-direction: column;
align-content: center;
}
.answer-button{
  width:200px;
}

</style>
