import React from 'react';
import {useLocation} from 'react-router-dom';
import ReactPlayer from 'react-player'

function VideoDetail(){

const location = useLocation();
const url = location.state.url;

return (
    <div>

    <h3> 비디오 재생 </h3>
         <ReactPlayer
            className="react-player"
            url={url}
            width="80%"
            height="80%"
            muted={true} //chrome정책으로 인해 자동 재생을 위해 mute 옵션을 true로 해주었다.
            playing={true}
            controls={true}
            style={{
                position: 'absolute',
                left:"10%"  
            }}
            loop={true} />


    </div>
)

}

export default VideoDetail;