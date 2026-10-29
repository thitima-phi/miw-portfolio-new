const projects = [
  { id: 'sonarcollection', company: 'sonar', title: 'A reason to press play.', cover: 'assets/drive/sonar-10.png', type: 'Book promotions', description: 'Book selections, best sellers and individual titles, brought into the feed with a clear listening message.', role: 'Promotional graphics & layout design' },
  { id: 'merick', company: 'merick', title: 'Technical products. Clearer stories.', cover: 'assets/drive/merick-32.png', type: 'Product communication', description: 'Product graphics for MERIBOOST and MAKSTIFF, turning technical information into visual communication.', role: 'Research, writing & graphic layouts' },
  { id: 'everyday', company: 'sonar', title: 'Everyday moments, more stories.', cover: 'assets/sonar/everyday-listening-2.png', type: 'Social content', description: 'Connecting audiobooks to familiar moments: getting ready, commuting and waiting for a ride.', role: 'Social media layouts & messaging' },
  { id: 'pigments', company: 'merick', title: 'Working with colour.', cover: 'assets/drive/merick-08.png', type: 'Photography & product graphics', description: 'Colour-sample photography and pigment layouts, with a separately labelled product-copy reference.', role: 'Product photography & graphic layouts' },
  { id: 'sonareducation', company: 'sonar', title: 'Making audiobooks feel familiar.', cover: 'assets/drive/sonar-18.png', type: 'Explainer content', description: 'What audiobooks are, how they compare with e-books, and where listening fits into everyday life.', role: 'Social graphics & visual explanations' },
  { id: 'sonarcarousel', company: 'sonar', title: 'A book, one swipe at a time.', cover: 'assets/drive/sonar-68.png', type: 'Carousel content', description: 'Two visual series for 100 นักฟิสิกส์พลิกโลก, pairing short reading prompts with book-led layouts.', role: 'Carousel graphics & promotional layouts' },
  { id: 'sherlock', company: 'sonar', title: 'A new case. A new listen.', cover: 'assets/sonar/sherlock-light.png', type: 'Book promotion', description: 'A paper-inspired promotional layout introducing a Sherlock Holmes audiobook.', role: 'Promotional layout & visual content' },
  { id: 'merickcampaigns', company: 'merick', title: 'Industry news, made readable.', cover: 'assets/drive/merick-43.png', type: 'Industry news', description: 'Packaging, plastics and sustainability stories with concise headlines and supporting imagery.', role: 'Content research, writing & graphic design' },
  { id: 'sonaroffers', company: 'sonar', title: 'A clear next step.', cover: 'assets/drive/sonar-13.png', type: 'Offers & app information', description: 'Subscription, free-trial and app-information designs that keep pricing and next steps easy to find.', role: 'Promotional layouts & app communication' },
  { id: 'pageupdates', company: 'merick', title: 'From the brief to the feed.', cover: 'assets/merick/page-preorder.webp', type: 'Published Facebook content', description: 'Published posts covering product availability, services and industry topics, showing copy and visuals in context.', role: 'Content research, writing & graphic design' },
  { id: 'everydaybeforeafter', company: 'sonar', title: 'A listening habit, reimagined.', cover: 'assets/sonar/everyday-listening-1.png', type: 'Social content', description: 'A before-and-after visual connecting everyday routines with audiobook listening.', role: 'Social media layout & messaging' },
  { id: 'america', company: 'sonar', title: 'One year. Another perspective.', cover: 'assets/sonar/sherlock-dark.png', type: 'Book promotion', description: 'A promotional layout for One Year in America, balancing book imagery with a listening invitation.', role: 'Promotional layout & visual content' },
  { id: 'poster', company: 'sonar', title: 'Meet your next listening habit.', cover: 'assets/sonar/listening-poster.png', type: 'Poster design', description: 'Everyday listening scenes and an app offer brought together in one promotional poster.', role: 'Poster layout & promotional design' },
  { id: 'landscape', company: 'sonar', title: 'Sherlock Holmes, ready to play.', cover: 'assets/sonar/sherlock-landscape.png', type: 'Release announcement', description: 'The audiobook release message adapted to a landscape canvas.', role: 'Promotional layout & format adaptation' },
  { id: 'sonarbanners', company: 'sonar', title: 'The message, in a wider format.', cover: 'assets/drive/sonar-25.png', type: 'Banner design', description: 'Two wider layouts for Sonar’s subscription and free-trial offers.', role: 'Banner layout & format adaptation' },
  { id: 'sonarvideo', company: 'sonar', title: 'Inside the recording studio.', cover: 'assets/drive/sonar-34-poster.jpg', type: 'Video content', description: 'Behind-the-scenes audiobook sessions and a short animated book-launch piece.', role: 'Selected video work from Sonar Audiobooks', video: true },
  { id: 'merickvideo', company: 'merick', title: 'Small samples. A moving story.', cover: 'assets/merick/merick-promotion-poster.jpg', type: 'Promotional video', description: 'Polymer pellets and colour samples in a short Facebook video, from planning the message to the final edit.', role: 'Planning, filming & CapCut editing', video: true }
];
const videoCollections = {
  sonarvideo: { title: 'Sonar Audiobooks · Recording & launch videos', items: [
    ['assets/drive/sonar-34.mp4', 'Behind the recording session · 2:11', 'assets/drive/sonar-34-poster.jpg'],
    ['assets/drive/sonar-35.mp4', 'Inside an audiobook session · 0:26', 'assets/drive/sonar-35-poster.jpg'],
    ['assets/drive/sonar-36.mp4', 'Exclusive book launch · 0:05', 'assets/drive/sonar-36-poster.jpg']
  ] },
  merickvideo: { title: 'Merick Polymers · Promotional video', items: [
    ['assets/merick/merick-promotion.mp4', 'Product samples promotional video · 0:51', 'assets/merick/merick-promotion-poster.jpg']
  ] }
};
const collections = { ...driveCollections, ...videoCollections };
const grid = document.querySelector('#project-grid');
const count = document.querySelector('#result-count');
for (const project of projects) {
  const article = document.createElement('article');
  article.className = 'project';
  article.dataset.company = project.company;
  const collection = collections[project.id];
  const company = project.company === 'sonar' ? 'SONAR AUDIOBOOKS' : 'MERICK & LEAF PAC';
  article.innerHTML = `<button class="project-cover" data-gallery="${project.id}" aria-label="${project.video ? 'Watch' : 'View'} ${project.type.toLowerCase()}"><img src="${project.cover}" alt="${collection.items.find(item => item[0] === project.cover)?.[1] || project.title}" loading="lazy" decoding="async"><span class="open-icon" aria-hidden="true">${project.video ? '▷' : '↗'}</span></button><div class="project-meta"><span>${company} / ${project.type.toUpperCase()}</span><span>${collection.items.length} ${project.video ? 'VIDEO' : 'ARTWORK'}${collection.items.length > 1 ? 'S' : ''}</span></div><h3>${project.title}</h3><p>${project.description}</p><p class="contribution">${project.video && project.company === 'sonar' ? '' : 'My contribution: '}${project.role}</p>`;
  grid.append(article);
}
count.textContent = `${projects.length} projects`;
document.querySelectorAll('[data-filter]').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('[data-filter]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    let visible = 0;
    grid.querySelectorAll('.project').forEach(project => {
      project.hidden = button.dataset.filter !== 'all' && project.dataset.company !== button.dataset.filter;
      if (!project.hidden) visible++;
    });
    count.textContent = `${visible} projects`;
  });
});
const dialog = document.querySelector('#gallery');
const image = document.querySelector('#gallery-image');
const video = document.querySelector('#gallery-video');
const previous = document.querySelector('#previous');
const next = document.querySelector('#next');
let activeCollection;
let activeIndex = 0;
function stopVideo() {
  video.pause();
  video.removeAttribute('src');
  video.load();
}
function renderGallery() {
  stopVideo();
  const [src, caption, poster] = activeCollection.items[activeIndex];
  const isVideo = src.endsWith('.mp4');
  image.hidden = isVideo;
  video.hidden = !isVideo;
  if (isVideo) {
    video.src = src;
    video.poster = poster;
    video.setAttribute('aria-label', caption);
  } else {
    image.src = src;
    image.alt = caption;
  }
  document.querySelector('#gallery-title').textContent = activeCollection.title;
  document.querySelector('#gallery-caption').textContent = caption;
  document.querySelector('#gallery-count').textContent = `${isVideo ? 'VIDEO' : 'ARTWORK'} ${activeIndex + 1} OF ${activeCollection.items.length}`;
  previous.disabled = activeIndex === 0;
  next.disabled = activeIndex === activeCollection.items.length - 1;
}
document.addEventListener('click', event => {
  const trigger = event.target.closest('[data-gallery]');
  if (!trigger) return;
  activeCollection = collections[trigger.dataset.gallery];
  activeIndex = 0;
  renderGallery();
  dialog.showModal();
});
previous.addEventListener('click', () => { if (activeIndex > 0) { activeIndex--; renderGallery(); } });
next.addEventListener('click', () => { if (activeIndex < activeCollection.items.length - 1) { activeIndex++; renderGallery(); } });
document.querySelector('#gallery-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('close', stopVideo);
dialog.addEventListener('click', event => {
  if (event.target !== dialog) return;
  const rect = dialog.getBoundingClientRect();
  if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
});
dialog.addEventListener('keydown', event => {
  if (event.target === video) return;
  if (event.key === 'ArrowLeft') previous.click();
  if (event.key === 'ArrowRight') next.click();
});
