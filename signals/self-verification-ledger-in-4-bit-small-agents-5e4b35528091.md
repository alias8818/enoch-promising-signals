# Self-Verification Ledger in 4-Bit Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-verification-ledger-in-4-bit-small-agents-5e4b35528091`
Run ID: `self-verification-ledger-in-4-bit-small-agents-5e4b35528091-20260526T041051226163+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/32cdf8380d92

## What looked useful

A self-verification ledger improved a naive 4-bit quantized proposer from 5.91% to 20.88% accuracy in the best bounded run, while float32 improved from 94.43% to 100.00%. The gain came mainly from invariant checks, and the ledger did not rescue the severe post-training 4-bit accuracy collapse.

## Boundaries and scale limits

Not a natural-language LLM test; no true 4-bit inference kernel; no quantization-aware training; task-specific arithmetic invariants are engineered and may not transfer to open-ended reasoning. Runs used at most 60k proposer training pairs, 80k verifier pairs, and 20k test pairs.

## Claim scope

Synthetic two-digit addition with small MLP proposer/verifier agents and explicit signed symmetric 4-bit post-training weight quantization. The ledger selects among proposer top-k candidates using verifier scores and arithmetic invariant checks.

## Why it stopped

Proxy evidence is mixed: ledger selection helps, but naive post-training 4-bit small agents remain unreliable, so the stronger hypothesis is not supported by this bounded experiment.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded test should use quantization-aware training or a true 4-bit small language model before evaluating ledger prompting claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware self-verification ledger for small arithmetic agents
- Success threshold: Quantization-aware 4-bit full-ledger accuracy >= 80% on 20,000 held-out examples and at least +10 percentage points over the 4-bit proposer-only baseline, with no more than 1% of baseline-correct answers broken.
- Stop condition: Stop as negative if quantization-aware 4-bit proposer top-k recall remains below 90% or full-ledger accuracy remains below 50% after one bounded GPU run under 30 minutes.

## Evidence references

- Artifact root: `<local-path>/projects/self-verification-ledger-in-4-bit-small-agents-5e4b35528091`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
