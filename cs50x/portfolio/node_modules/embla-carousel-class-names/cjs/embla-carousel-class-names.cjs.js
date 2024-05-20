'use strict';

const defaultOptions = {
  active: true,
  breakpoints: {},
  snapped: 'is-snapped',
  inView: 'is-in-view',
  draggable: 'is-draggable',
  dragging: 'is-dragging'
};

function removeClass(node, className) {
  if (!node || !className) return;
  const {
    classList
  } = node;
  if (classList.contains(className)) classList.remove(className);
}
function addClass(node, className) {
  if (!node || !className) return;
  const {
    classList
  } = node;
  if (!classList.contains(className)) classList.add(className);
}
function nodeListToArray(nodeList) {
  return Array.from(nodeList);
}

function ClassNames(userOptions = {}) {
  let options;
  let emblaApi;
  let root;
  let slides;
  const selectedEvents = ['select'];
  const draggingEvents = ['pointerDown', 'pointerUp'];
  const inViewEvents = ['slidesInView'];
  function init(emblaApiInstance, optionsHandler) {
    emblaApi = emblaApiInstance;
    const {
      mergeOptions,
      optionsAtMedia
    } = optionsHandler;
    const optionsBase = mergeOptions(defaultOptions, ClassNames.globalOptions);
    const allOptions = mergeOptions(optionsBase, userOptions);
    options = optionsAtMedia(allOptions);
    root = emblaApi.rootNode();
    slides = emblaApi.slideNodes();
    const isDraggable = !!emblaApi.internalEngine().options.watchDrag;
    if (isDraggable) {
      addClass(root, options.draggable);
    }
    if (options.dragging) {
      draggingEvents.forEach(evt => emblaApi.on(evt, toggleDraggingClass));
    }
    if (options.snapped) {
      selectedEvents.forEach(evt => emblaApi.on(evt, toggleSnappedClasses));
      toggleSnappedClasses();
    }
    if (options.inView) {
      inViewEvents.forEach(evt => emblaApi.on(evt, toggleInViewClasses));
      toggleInViewClasses();
    }
  }
  function destroy() {
    removeClass(root, options.draggable);
    draggingEvents.forEach(evt => emblaApi.off(evt, toggleDraggingClass));
    selectedEvents.forEach(evt => emblaApi.off(evt, toggleSnappedClasses));
    inViewEvents.forEach(evt => emblaApi.off(evt, toggleInViewClasses));
    slides.forEach(slide => removeClass(slide, options.snapped));
  }
  function toggleDraggingClass(_, evt) {
    if (evt === 'pointerDown') addClass(root, options.dragging);else removeClass(root, options.dragging);
  }
  function toggleSlideClasses(slideIndexes, className) {
    const container = emblaApi.containerNode();
    const slideNodeList = container.querySelectorAll(`.${className}`);
    const removeClassSlides = nodeListToArray(slideNodeList);
    removeClassSlides.forEach(slide => removeClass(slide, className));
    slideIndexes.forEach(index => addClass(slides[index], className));
  }
  function toggleSnappedClasses() {
    const {
      slideRegistry
    } = emblaApi.internalEngine();
    const slideIndexes = slideRegistry[emblaApi.selectedScrollSnap()];
    toggleSlideClasses(slideIndexes, options.snapped);
  }
  function toggleInViewClasses() {
    const slideIndexes = emblaApi.slidesInView();
    toggleSlideClasses(slideIndexes, options.inView);
  }
  const self = {
    name: 'classNames',
    options: userOptions,
    init,
    destroy
  };
  return self;
}
ClassNames.globalOptions = undefined;

module.exports = ClassNames;
//# sourceMappingURL=embla-carousel-class-names.cjs.js.map
