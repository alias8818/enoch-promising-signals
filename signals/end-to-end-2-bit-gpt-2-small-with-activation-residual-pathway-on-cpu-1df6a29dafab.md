# End-to-end 2-bit GPT-2-small with activation residual pathway on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-2-bit-gpt-2-small-with-activation-residual-pathway-on-cpu-1df6a29dafab`
Run ID: `end-to-end-2-bit-gpt-2-small-with-activation-residual-pathway-on-cpu-1df6a29dafab-20260621T224304611357+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1bcbea3c9b85

## What looked useful

The compact rank-64 residual path did not improve dense-logit relative L2 or cosine at GPT-2-small shape. A high rank-512 residual path improved relative L2 from 1.1609 to 0.9242, but required about 60.3% of dense theoretical storage and did not materially recover next-token ranking. The simple coordinate-basis activation residual mechanism is therefore not sufficient under this bounded proxy.

## Boundaries and scale limits

No pretrained GPT-2 weights, no language-model perplexity, no full 50257-token vocabulary, no training or fine-tuning, no packed int2 CPU kernels, one seed, batch 1, sequence length 32. This is an early mechanism/fidelity probe, not full GPT-2 validation.

## Claim scope

Bounded CPU proxy on a NumPy GPT-2-small-shape random-weight transformer: 12 layers, d_model 768, 12 heads, MLP width 3072, seq_len 32, vocab 8192. Tested signed rowwise 2-bit linear weights plus coordinate-basis activation residual correction at ranks 64, 256, and 512 against dense-logit recovery.

## Why it stopped

Proxy/early falsification: the tested residual path did not produce viable dense-logit or ranking recovery at compact rank, and high-rank recovery gave back too much storage while remaining ranking-poor.

## Recommended next action

Stop this run as a no-paper useful-signal negative; if continuing, run a bounded pretrained GPT-2-small follow-up with learned residual bases and validation perplexity controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small 2-bit residual-basis validation
- Success threshold: At no more than 35% of dense theoretical weight storage, int2 plus residual should recover at least 90% of dense-vs-int2 perplexity degradation and reach at least 0.50 top-5 overlap with dense logits on the fixed validation shard.
- Stop condition: Stop if the learned residual path cannot beat the int2 baseline by at least 25% relative reduction in perplexity degradation or if the storage budget required for recovery exceeds 50% of dense weights.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-2-bit-gpt-2-small-with-activation-residual-pathway-on-cpu-1df6a29dafab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
