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
                <div style={{display:"flex"}}>
                    <h1 id={"hamburger"} style={
                        {
                            fontSize:"32px",
                            padding:".2em .2em"
                        }
                    }>≡</h1>
                    <h1 style={{
                        fontSize:"32px",
                        margin:"auto auto"
                    }}>dfjsakl (i am aware that the website sucks)</h1>
                </div>
            )
    }
}


const domContainer = document.querySelector('#nav-div')
const root = ReactDOM.createRoot(domContainer);
root.render(React.createElement(NavBar));