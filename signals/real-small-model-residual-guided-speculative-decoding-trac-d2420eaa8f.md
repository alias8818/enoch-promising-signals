# Real Small-Model Residual-Guided Speculative Decoding Trace Test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-small-model-residual-guided-speculative-decoding-trac-d2420eaa8f`
Run ID: `real-small-model-residual-guided-speculative-decoding-trac-d2420eaa8f-20260528T024204955479+0000`

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

- Parent run decision: Residual-Channel-Guided Speculative Decoding on CPU: enoch://control-plane/projects/residual-channel-guided-speculative-decoding-on-cpu-0ea944eccf5a/runs/residual-channel-guided-speculative-decoding-on-cpu-0ea944eccf5a-20260527T232330933386+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/98c7eafd6b81

## What looked useful

Residual-guided proposals improved expected acceptance by +11.31 percentage points and KL by -2.87 for tiny-gpt2 -> distilgpt2. For the closer distilgpt2 -> gpt2 pair, they improved expected acceptance by +1.65 points and KL by -0.033, but missed the predeclared +2 point acceptance threshold.

## Boundaries and scale limits

Trace-only CPU inference on fixed short English passages; no end-to-end speculative decoder, no throughput measurement, no generated continuations, no large target models, no broad corpus robustness, and no learned residual predictor.

## Claim scope

On 104 real text prefix positions per model pair, a simple causal EMA of target-minus-draft logits improved exact one-step speculative proposal quality for GPT-2-family models; the effect was strong for sshleifer/tiny-gpt2 -> distilgpt2 and smaller for distilgpt2 -> gpt2.

## Why it stopped

No-paper useful signal: direct small trace evidence supports the residual mechanism in a weak-draft setting, but the closer practical pair missed the predeclared acceptance threshold and no end-to-end decoding speed evidence was produced.

## Recommended next action

Run a bounded deepen test on 1000-5000 held-out prefixes with at least two real draft-target size gaps and an end-to-end speculative decoding check only if the closer-model acceptance delta reaches at least 2 percentage points with nonworse KL.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-Scale Residual-Guided Speculative Decoding Trace and Decoder Check
- Success threshold: Mean expected acceptance improves by at least 0.02 with nonworse KL on each close-model pair, paired 95% confidence interval lower bound is above 0 for acceptance delta, and end-to-end decoding throughput improves by at least 5% after residual overhead.
- Stop condition: Stop if close-model trace acceptance delta remains below 0.02, KL worsens, or residual bookkeeping overhead eliminates the measured decoding throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-model-residual-guided-speculative-decoding-trac-d2420eaa8f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
