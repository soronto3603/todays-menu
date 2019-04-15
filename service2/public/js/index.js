let menu = [
    "떡볶이",
    "피자",
    "치킨",
    "파스타",
    "스테이크",
    "짜장면",
    "짬뽕",
    "탕수육",
    "덮밥",
    "오므라이스",
    "샐러드",
    "김밥",
    "라면",
    "어묵",
    "국수",
    "냉면",
    "만두",
    "떡국",
    "파전 with 막걸리",
    "고기",
    "라면",
    "제육볶음",
    "초밥",
    "비빔밥",
    "불고기",
    "국밥",
    "쭈꾸미 볶음",
    "굶어",
    "족발",
    "보쌈",
    "돈까스",
    "부대찌개",
    "도시락",
    "순대",
    "매운닭발",
    "튀김",
    "쫄면",
    "함박스테이크"
];

const contents_animation = (text)=>{
    $("#main").text(text);
    $("#contents").css({display:"block"});
    $("#contents").animate({opacity:1,bottom:"+=50"},1000)
};
const contents_reset = ()=>{
    $("#contents").css({opacity:0,bottom:-50,display:"none"})
};
const contents2_animation = (text)=>{
    $("#text2").text(text);
    $("#contents2").css({display:"block"});
    $("#contents2").animate({opacity:1,bottom:"+=50"},1000)
};
const contents2_reset = ()=>{
    $("#contents2").css({opacity:0,bottom:-50,display:"none"})
}

const contents3_animation = (text)=>{
    $("#text3").text(text);
    $("#contents3").css({display:"block"});
    $("#contents3").animate({opacity:1,bottom:"+=50"},1000)
}
const contents3_reset = ()=>{
    $("#contents3").css({opacity:0,bottom:-50,display:"none"})
}
const contents4_animation = (text)=>{
    $("#text4").text(text);
    $("#contents4").css({display:"block"});
    $("#contents4").animate({opacity:1,bottom:"+=50"},1000)
}
const contents4_reset = ()=>{
    $("#contents4").css({opacity:0,bottom:-50,display:"none"})
}

window.onload=(r)=>{
    setTimeout(()=>{
        contents_animation("Hello");
    },0);
    setTimeout(()=>{
        contents_reset();
    },1500);
    setTimeout(()=>{
        contents2_animation(`
            본 서비스는
            점심메뉴를 정해주는 딥러닝 프로그램을 만들고자
            데이터를 수집하기 위한 서비스 입니다.

            앞으로 제공되는 질문은 서버에 데이터가 저장될 수 있으며,
            개인정보는 저장하지 않습니다.
        `);
    },1500);
    

}
const not = ()=>{
    setTimeout(()=>{
        contents2_reset();
    },0)
    setTimeout(()=>{
        contents_animation("Good Bye!");
    },0);
}
const agree = ()=>{
    setTimeout(()=>{
        contents2_reset();
    },0)
    setTimeout(()=>{
        contents3_animation("지금 기분이 어때요?");
    },0)
}

const prediction = ()=>{
    setTimeout(()=>{
        contents3_reset();
    },0)
    setTimeout(()=>{
        contents4_animation("** 어떠세요?");
    },0)
}
const retry = ()=>{
    setTimeout(()=>{
        contents4_reset();
    },0)
    setTimeout(()=>{
        contents3_animation("지금 기분이 어때요?");
    },0)
}
const finish = ()=>{
    setTimeout(()=>{
        contents4_reset();
    },0)
    setTimeout(()=>{
        contents_animation("Good Bye!");
    },0)
}