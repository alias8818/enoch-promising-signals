# Proxy-Loss Domain Reweighting for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proxy-loss-domain-reweighting-for-tiny-pretraining-fe8b480388b4`
Run ID: `proxy-loss-domain-reweighting-for-tiny-pretraining-fe8b480388b4-20260609T203710205804+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e1d7582ea778

## What looked useful

Absolute proxy loss is not a safe standalone domain reward when high loss can reflect irreducible entropy. Target-domain filtering changed the same mechanism from harmful to helpful in this bounded test: proxy_loss_all was +0.2069 target-loss worse than uniform and sampled 85.4% IID noise, while proxy_loss_target_only was -0.0490 target-loss better than uniform and sampled no IID noise.

## Boundaries and scale limits

Synthetic token generators, one-layer GRU tiny LM, 700 optimizer steps per run, four seeds, training-model validation loss used as the proxy signal; no real corpus, tokenizer, separate proxy model, transformer baseline, or long-scale pretraining validation.

## Claim scope

In a synthetic three-domain tiny language-model pretraining test, naive absolute proxy-loss sampling over all domains over-sampled an irreducible IID-noise domain and hurt target loss, while proxy-loss sampling restricted to target-aligned domains improved target loss versus uniform across four seeds.

## Why it stopped

Bounded synthetic evidence produced a mechanism diagnostic but not direct publication-grade evidence for tiny pretraining on real data.

## Recommended next action

Stop this run as no-paper useful signal; next run should test entropy-normalized or improvement-based proxy reweighting on a small real-corpus setup with a separate proxy model and matched-token baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Entropy-normalized proxy reweighting on small real-corpus tiny pretraining
- Success threshold: Entropy-normalized or loss-improvement proxy policy improves target validation loss by at least 2% versus uniform and avoids allocating more than 20% of samples to the high-entropy control domain when that domain is outside the target mixture.
- Stop condition: Stop if absolute-loss proxy again allocates most samples to high-entropy noise and corrected proxy policies fail to beat uniform by at least 1% target validation loss over three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-loss-domain-reweighting-for-tiny-pretraining-fe8b480388b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
