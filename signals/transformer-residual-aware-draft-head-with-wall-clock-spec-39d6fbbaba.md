# Transformer residual-aware draft head with wall-clock speculative decode metrics

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `transformer-residual-aware-draft-head-with-wall-clock-spec-39d6fbbaba`
Run ID: `transformer-residual-aware-draft-head-with-wall-clock-spec-39d6fbbaba-20260527T203043356155+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Parameter-matched residual-aware draft head with acceptance-length metrics: enoch://control-plane/projects/parameter-matched-residual-aware-draft-head-with-acceptanc-769f07a463/runs/parameter-matched-residual-aware-draft-head-with-acceptanc-769f07a463-20260527T165351079177+0000
- Parent run decision: Residual-Aware Draft Head on a Small Real Transformer: enoch://control-plane/projects/residual-aware-draft-head-on-a-small-real-transformer-541bcfe9a6/runs/residual-aware-draft-head-on-a-small-real-transformer-541bcfe9a6-20260527T084803328421+0000

## What looked useful

Residual-aware heads produced high acceptance (best residual_hidden block 4: 0.983; best direct_logits block 8: 0.918) and high target-pass economy (up to 8.34 tokens/pass), but the best non-oracle wall-clock result was only 0.687x greedy target speed and even the oracle control reached only 0.775x. The mechanism signal is real in the toy residual tower, but wall-clock overhead dominates.

## Boundaries and scale limits

CPU-only worker, no GPU, no PyTorch/Transformers, synthetic residual tower rather than GPT-2-small or pretrained transformer, no tokenizer/natural-language corpus, no attention KV cache, and no GPU serving kernels. Full-run validation was five fixed seeds, 3,072 measured tokens per seed, blocks 2/4/8.

## Claim scope

On a synthetic NumPy residual-tower autoregressive model, residual-aware draft heads improve acceptance and emitted tokens per target verification pass over a tied intermediate head, but do not improve wall-clock tokens/sec versus greedy target decoding.

## Why it stopped

Bounded direct wall-clock validation on the local CPU residual-tower harness failed the practical speedup threshold: all residual-aware draft configurations were slower than greedy target decoding, and the oracle control was also slower, so mechanism support did not translate to wall-clock speculative decode speed.

## Recommended next action

Stop this branch as no-paper evidence unless a GPU/KV-cache pretrained-transformer implementation first shows that an oracle or near-oracle draft can exceed greedy wall-clock throughput under the same measurement protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache pretrained-transformer residual draft head wall-clock gate
- Success threshold: Across at least 5 fixed seeds/prompts, oracle speculative decoding must exceed greedy by >=1.10x wall-clock tokens/sec, and the best residual-aware head must exceed greedy by >=1.05x while improving acceptance by >=25 percentage points over tied intermediate head.
- Stop condition: Stop early if oracle speculative decoding is <=1.05x greedy wall-clock throughput on the pretrained/KV-cache implementation, because draft-head improvements cannot overcome system overhead under that setup.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-residual-aware-draft-head-with-wall-clock-spec-39d6fbbaba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
