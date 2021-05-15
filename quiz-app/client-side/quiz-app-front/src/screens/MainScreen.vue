<template>
    <div>
    <Header title="Quiz-App4"/>
    <QuizPanel/>
    <StartPanel/>
    </div>
</template>
<script>
import Header from "../components/Header"
//import StartPanel from "./panels/StartPanel"
import QuizPanel from "./panels/QuizPanel"
import StartPanel from './panels/StartPanel.vue'
export default
{
    name:"MainScreen",
    props: ["userName"],
    components :{
        Header,StartPanel,QuizPanel
    }
}
</script>
