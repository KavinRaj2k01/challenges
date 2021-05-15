<template>
    <div>
    <Header title="Quiz-App4"/>
    <StartPanel :onclickStart="onclickStart"  v-if="state.panel==='Start'" />
    <QuizPanel v-if="state.panel==='Quiz'"/>
    </div>
</template>
<script>
import Header from "../components/Header"
//import StartPanel from "./panels/StartPanel"
import QuizPanel from "./panels/QuizPanel"
import StartPanel from './panels/StartPanel.vue'

const screens={start: "Start", quiz:"Quiz"}
const func=function()
{
    return "Kavin"
}
func();
export default
{
    name:"MainScreen",
    props: ["userName"],
    components :{
        Header,StartPanel,QuizPanel
    },
    data : function(){ return {state: {panel: screens.start}, onclickStart: () => alert('Start Clicked!')}}
    //{ state : {panel: screens.start}}
}
</script>
