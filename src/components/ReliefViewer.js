import React, { useEffect, useRef } from 'react';
import * as BABYLON from 'babylonjs';

const ReliefViewer = ({ ascFile }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const engine = new BABYLON.Engine(canvas, true);

    const createScene = () => {
      const scene = new BABYLON.Scene(engine);

      // Load the ASC file
      BABYLON.SceneLoader.ImportMesh("", "", ascFile, scene, function(newMeshes) {
        // Position the camera to view the scene
        scene.createDefaultCameraOrLight(true, true, true);
        scene.activeCamera.alpha += Math.PI;
        scene.activeCamera.beta += Math.PI/2;
      });

      return scene;
    };

    const scene = createScene();

    // Start the render loop
    engine.runRenderLoop(() => {
      if (scene) {
        scene.render();
      }
    });

    // Resize the canvas when the window is resized
    const resizeCanvas = () => {
      canvas.width = canvas.clientWidth;
      canvas.height = canvas.clientHeight;
      engine.resize();
    };
    window.addEventListener('resize', resizeCanvas);

    // Clean up
    return () => {
      window.removeEventListener('resize', resizeCanvas);
      scene.dispose();
      engine.dispose();
    };
  }, [ascFile]);

  return <canvas ref={canvasRef} />;
};

export default ReliefViewer;
