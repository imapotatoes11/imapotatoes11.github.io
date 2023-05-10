// 'use strict';

class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.args = {
            dark:false,
            mobile:false
        }
        if (navigator.userAgent.match(/Android/i)
            || navigator.userAgent.match(/webOS/i)
            || navigator.userAgent.match(/iPhone/i)
            || navigator.userAgent.match(/iPad/i)
            || navigator.userAgent.match(/iPod/i)
            || navigator.userAgent.match(/BlackBerry/i)
            || navigator.userAgent.match(/Windows Phone/i))
            this.args.mobile = true
    }
    render(){
        if (this.args.mobile && !this.args.dark)
            return (<div>adsfjl</div>)
        else if (this.args.mobile && this.args.dark)
            return (<div>dark_adsfjl</div>)
        else if (!this.args.mobile && this.args.dark)
            return (<div>dark_adsfasdfkljasdfjl</div>)
        else
            return (
                <div style={{
                    display:"flex",
                    padding:"2em",
                    margin:"0",
                    background:"white",
                    fontFamily:"'SF Pro Text', 'SF Pro Icons'",
                    zIndex:"-1"
                }}>
                    {/*<h1 id={"hamburger"} style={*/}
                    {/*    {*/}
                    {/*        fontSize:"32px",*/}
                    {/*        padding:".2em .2em"*/}
                    {/*    }*/}
                    {/*}>≡</h1>*/}
                    <h1 style={{
                        fontSize:"32px",
                        position:"fixed",
                        margin:"auto auto",
                        // left: "50%",
                        top: "3.5%",
                        // transform: "translate(-50%)",
                        color:"var(--text-color)",
                        cursor:"pointer"
                    }} onClick={()=>{window.location.href="#"}}>mmm yes</h1>
                    <div className={"nav-items"}>
                        <a className={"nav-item"} href={"#"}>Home</a>
                        <a className={"nav-item"} href={"#"}>About</a>
                        <a className={"nav-item"} href={"#"}>Projects</a>
                        <a className={"nav-item"} href={"https://rickrollredirect.github.io"}>Contact</a>
                    </div>
                </div>
            )
    }
}


const domContainer = document.querySelector('#nav-div')
const root = ReactDOM.createRoot(domContainer);
root.render(React.createElement(NavBar));