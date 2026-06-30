# Layer-skip self-speculative decoding on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-skip-self-speculative-decoding-on-gb10-4c0043f954be`
Run ID: `layer-skip-self-speculative-decoding-on-gb10-4c0043f954be-20260620T051532017533+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1ff5a6bb3738

## What looked useful

Dense baseline exit-2/final top-1 agreement was 0.0662 and self-spec acceptance was 0.0172; LayerSkip-style training raised exit-2/final agreement to 0.9815 and self-spec acceptance to 1.0 with exact greedy output preservation and 75% fewer full-model calls on the measured generation.

## Boundaries and scale limits

The intended real-checkpoint test against facebook/layerskip-llama3.2-1B was blocked by gated Hugging Face access. The completed result is synthetic/toy-scale, unoptimized, and not a natural-language or 1B/7B validation.

## Claim scope

A controlled 4-layer toy causal Transformer on GB10 showed that LayerSkip-style early-exit losses plus progressive layer dropout can make an intermediate layer usable for exact greedy self-speculative decoding, unlike a same-size dense final-loss baseline.

## Why it stopped

Direct LayerSkip Llama validation was blocked by gated checkpoint access, and the successful local evidence is a synthetic proxy rather than publication-grade natural-language evidence.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with an accessible real language checkpoint or a bounded locally trained small language model that can report quality, acceptance, and optimized throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded real-language LayerSkip self-speculative decoding on an accessible small checkpoint
- Success threshold: Exit layer chosen before the final quarter of layers reaches at least 0.80 top-1 agreement with the final layer, at least 0.70 self-spec acceptance, exact greedy equivalence on all measured prompts, and at least 1.10x tokens/sec versus greedy autoregressive decoding.
- Stop condition: Stop as negative if the dense baseline and early-exit model differ by less than 0.10 agreement, if self-spec acceptance stays below 0.50, or if exact greedy equivalence fails under deterministic decoding.

## Evidence references

- Artifact root: `<local-path>/projects/layer-skip-self-speculative-decoding-on-gb10-4c0043f954be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
