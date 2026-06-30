# Coherence-Scored Data Selection for Long-Context Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `coherence-scored-data-selection-for-long-context-pretraining-9d82ff00480b`
Run ID: `coherence-scored-data-selection-for-long-context-pretraining-9d82ff00480b-20260628T072310607546+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b49dbf04196f

## What looked useful

Coherence-top selection chose 100% coherent documents and reached 1.0000 held-out answer accuracy versus 0.1257 for random and 0.0326 for coherence-bottom. Low-coherence selection worsened held-out LM loss versus random, but coherence-top did not improve aggregate LM loss versus random, so the supported mechanism is long-range retrieval rather than universal perplexity improvement.

## Boundaries and scale limits

Single synthetic generator, one random seed for the main corrected run, tiny 2-layer 96-hidden causal Transformer, sequence length 256, 2,000 steps per selector, no natural text, no downstream benchmarks, no large-model or multi-node training.

## Claim scope

Synthetic fixed-token long-context pretraining probe: coherence-score selection can improve held-out long-range query-answer accuracy when the corpus mixes coherent topic/fact-consistent documents with corrupted low-coherence documents.

## Why it stopped

No-paper closure: this is a proxy synthetic useful signal, not direct validation of real long-context pretraining.

## Recommended next action

Run a bounded deepen experiment with multiple seeds and a semi-natural or real text corpus using coherence scoring against length, random, and perplexity/dedup baselines before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed semi-natural coherence selection for long-context retrieval
- Success threshold: Coherence selection improves held-out long-context retrieval accuracy by at least 10 absolute percentage points over the best non-oracle baseline with no more than 5% relative degradation in aggregate validation loss in at least 2 of 3 seeds.
- Stop condition: Stop as negative if coherence selection fails to beat the best non-oracle baseline on retrieval in at least 2 of 3 seeds or if gains only appear when the score directly encodes the validation answers.

## Evidence references

- Artifact root: `<local-path>/projects/coherence-scored-data-selection-for-long-context-pretraining-9d82ff00480b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
