# Self-speculative decode using mid-layer hidden states

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decode-using-mid-layer-hidden-states-28f9397d245a`
Run ID: `self-speculative-decode-using-mid-layer-hidden-states-28f9397d245a-20260601T043611683597+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e2ed0cb03f27

## What looked useful

Frozen final-head projection peaked at 0.832x approximate speedup despite 52.6% top-1 agreement at layer 5. A trained Linear(768,768) map from layer-1 hidden states to final normalized hidden states reached 60.94% held-out top-1 agreement and 1.189x approximate speedup at gamma=4 on held-out prompts.

## Boundaries and scale limits

Tested only distilgpt2, 24 short prompts, greedy decoding, simulated verification, and modeled draft cost. No actual early-exit KV-cache implementation, wall-clock serving benchmark, broad corpus, GPT-2-small-class baseline, or 7B-class validation was run.

## Claim scope

On distilgpt2 greedy continuations, frozen mid-layer states projected through the existing final head are not efficient for self-speculative decoding, but a trained layer-1 linear hidden-state alignment head produced a bounded held-out mechanism signal with approximate speedup above 1 under a layer-fraction draft-cost model.

## Why it stopped

Current evidence is bounded and partly proxy-based: it directly measures agreement and greedy speculative acceptance, but speedup is modeled rather than measured in an actual early-exit decoder.

## Recommended next action

Stop this run as no-paper useful signal; next implement a real early-exit draft path with KV-cache reuse and measure wall-clock tokens/s on GPT-2-small-class models before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Wall-clock early-exit self-speculative decoding with trained layer-1 alignment heads
- Success threshold: Measured end-to-end tokens/s speedup >= 1.05x versus standard greedy decoding while matching greedy outputs exactly on the evaluated corpus.
- Stop condition: Stop if measured speedup is <= 1.0x after a correct cached early-exit implementation, or if acceptance falls below 25% drafted-token acceptance on held-out benchmark text.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decode-using-mid-layer-hidden-states-28f9397d245a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
