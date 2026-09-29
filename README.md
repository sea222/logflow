# LogFlow (Python) — Artırım 1: İskelet Hat

Bir log dosyasını **hat (pipeline)** üzerinden okuyup konsola yazar.

## Çalıştırma (Python 3.8+, ek paket gerekmez)

    python main.py data/access-small.log      # Windows
    python3 main.py data/access-small.log     # macOS / Linux

## Sözlük
| Terim | Anlamı |
|---|---|
| Record | Hattan akan veri birimi (bu hafta `str`) |
| Stage | Kaydı işleyen, 0/1/N çıktı üretebilen bileşen |
| Source | Kayıt üreten uç (`FileLineSource`) |
| Sink | Kayıt tüketen uç (`ConsoleSink`) |
| Pipeline | Source → Stage'ler → Sink zincirini kurup çalıştırır |

## Dizin
    logflow/   emitter, stage, source, sink (arayüzler), file_line_source, console_sink, pipeline
    main.py    yalnızca: argüman oku, hattı kur, run()
    data/      access-small.log (200 satır)

## Tasarım notu
`Stage.process` değer döndürmez, `Emitter` üzerinden yayar: bir filtre girdi başına
0, 1 veya N çıktı üretebilir; dönüş değeri 1:1'e zorlar.

S�rüm: `v1`
