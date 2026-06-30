# Early-Exit Layer as Zero-Cost Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `early-exit-layer-as-zero-cost-draft-model-335a1bda8cae`
Run ID: `early-exit-layer-as-zero-cost-draft-model-335a1bda8cae-20260531T211930884338+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/435fc4b4d6a3

## What looked useful

Multi-token early-layer drafts were rejected too often to break even: for draft_k=4, all tested layers had idealized speedup below 1.0, best 0.713x at layer 2. The most favorable one-token layer-1 case reached only 1.096x idealized speedup, a margin likely vulnerable to implementation overhead.

## Boundaries and scale limits

Tested one pretrained 12-layer GPT-2 model, 64 built-in prompts at most, greedy decoding only, no real early-stop/KV-cache wall-clock implementation, no trained auxiliary heads, no large-model or long-context validation.

## Claim scope

On GPT-2-small with greedy decoding, short prompts, raw intermediate hidden states projected through the final LM head are not a practical multi-token zero-cost draft model; a one-token layer-1/2 variant only barely breaks even in an optimistic layer-count model.

## Why it stopped

Bounded direct GPT-2-small evidence falsified practical multi-token usefulness, and the only positive one-token signal was proxy/idealized and too small for a paper claim.

## Recommended next action

Stop this raw early-hidden-state plus final-head version as no-paper evidence; the bounded next test, if pursued, is confidence-gated or auxiliary-head self-speculation on GPT-2-small with real wall-clock measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-Gated Early-Exit Drafting on GPT-2-Small
- Success threshold: At least 1.15x wall-clock tokens/sec over full-model greedy decoding while preserving exact greedy target outputs, with gate coverage at or above 25% of generated positions.
- Stop condition: Stop if gated layer-1/2 drafting is below 1.05x wall-clock speedup or below 15% gate coverage after tuning only thresholds on a held-out prompt split.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-layer-as-zero-cost-draft-model-335a1bda8cae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
