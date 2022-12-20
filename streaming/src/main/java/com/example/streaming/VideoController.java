package com.example.streaming;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
// import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;
@RestController
@RequestMapping(path = "video")
@RequiredArgsConstructor
public class VideoController {

    @Autowired
    private final VideoService videoService;

    private final VideoRepository videoRepository;
    @CrossOrigin("*")
    @GetMapping("list")
    public List<Video> showVideoList(){
        List<Video> videos = videoRepository.findAll();
        
        return videos;

    }

    @CrossOrigin("*")    
    @GetMapping("{videoTitle}")
    public String video(@PathVariable String videoTitle){
        Video video = videoRepository.findByTitle(videoTitle);
        
        return video.toString();
    }


}
