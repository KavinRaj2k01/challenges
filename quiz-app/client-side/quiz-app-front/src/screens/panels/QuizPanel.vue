<template>
    <div>
        <h4 > Question No :{{quizNo}}</h4>
        <p> {{quizContent}} </p>
        <div class='answer-container'>
          <ButtonGroup   :onClickOption="onclick" :options="options" />
        </div>
    </div>
</template>
<script>
import ButtonGroup from "../../components/ButtonGroup"

export default{
    name:"QuizPanel",
    props:["quizNo","quizContent","quizOptions","quizAnswer","onQuizAnswer"],
    components:{
      ButtonGroup
    },
    methods:{onclick:function(event)
    {
      if(event.target.value===this.quizAnswer)
      {
        this.onQuizAnswer(true,event.target.value);
      }
      else{
        this.onQuizAnswer(false,event.target.value);
      }
    }},
    data:function(){
      let options=[];
      for(let i=0;i<this.quizOptions.length;i++)
      {
        const option={label:this.quizOptions[i],value:this.quizOptions[i], disabled:false};
        options.push(option);
      }
      console.log(options);
      return {options:options}
    }
}
</script>

<style >
.answer-container
{
display:flex;  
flex-direction: column;
align-items: center;
}
.answer-button{
  width:200px;
  height:50px;
  margin:10px;
  border-radius:10px;
}

</style>
