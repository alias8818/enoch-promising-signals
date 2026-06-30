# Activation Steering Refusal for Safer 2-Layer Home Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-steering-refusal-for-safer-2-layer-home-agents-1f70b4fbfc07`
Run ID: `activation-steering-refusal-for-safer-2-layer-home-agents-1f70b4fbfc07-20260529T091717719308+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/22ed60cbac84

## What looked useful

Positive refusal-direction steering raised mean unsafe refusal from 0.347 to 0.507 at alpha 3 and safety-utility score from 0.210 to 0.264, beating best random-direction control at 0.227, but benign correctness fell from 0.648 to 0.562 and over-refusal rose from 0.162 to 0.248.

## Boundaries and scale limits

Synthetic template data, 5 random seeds, 36 OOD test commands per seed, classifier hidden states only; no LLM residual-stream activations, real home-agent traces, tool execution, multi-turn context, or human safety labels.

## Claim scope

In a synthetic two-layer MLP home-command policy, a mean hidden-activation refusal direction can increase unsafe-command refusal relative to no steering and random-direction controls, but with a measurable benign over-refusal tradeoff.

## Why it stopped

No-paper closure: this was a synthetic/proxy mechanism test with high seed variance and a clear over-refusal tradeoff, not a full validation of safer two-layer home agents.

## Recommended next action

Run a bounded direct-evidence follow-up on a small local LLM home-agent scaffold with activation capture, prompt/classifier/logit-bias baselines, and a fixed benign over-refusal ceiling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM activation steering refusal in a two-layer home-agent scaffold
- Success threshold: At least 20 percentage-point reduction in unsafe tool-call attempts versus the strongest non-activation baseline, with benign over-refusal <= 10% and confidence intervals that exclude zero improvement.
- Stop condition: Stop if activation steering fails to beat prompt/classifier/logit-bias baselines under the over-refusal ceiling on the held-out prompt suite.

## Evidence references

- Artifact root: `<local-path>/projects/activation-steering-refusal-for-safer-2-layer-home-agents-1f70b4fbfc07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
