# ARCHITECTURE — Artırım 1

**Arayüz** ne yapılacağını, **uygulama** nasıl yapıldığını söyler. `Pipeline` yalnızca
`Source` ve `Sink` arayüzlerini bilir.

## İki Kutu Diyagramı

    +-----------------------+      Emitter.emit(str)      +-----------------------+
    |    FileLineSource     | --------------------------> |      ConsoleSink      |
    |    (extends Source)   |   (bağlayıcı / connector)   |     (extends Sink)    |
    +-----------------------+                             +-----------------------+
              ^                                                     ^
              +------------- Pipeline: Source -> [Stage ...] -> Sink -+

## Bileşenler
Source.produce(out) · Stage.process(item, out) / open / close · Sink.consume(item) ·
Emitter.emit(item) · Pipeline.run()

## Bağlayıcılar
Bileşenler birbirini doğrudan çağırmaz, `Emitter` üzerinden konuşur.
`run()` zinciri sondan başa kurar: sink ← stage[n-1] ← … ← stage[0] ← source.

## Kararlar
1. Emitter, dönüş değeri yerine: 0/1/N çıktı esnekliği.
2. Küçük arayüzler, tek sorumluluk.
3. Main'de iş mantığı yok.
4. Bu hafta hattın değeri görünmez (çıktı = girdi); değer sonraki artırımlarda,
   Pipeline'a dokunmadan stage eklenince ortaya çıkar.
