# Parameter-matched mini-GPT-2 HMT language-model validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `parameter-matched-mini-gpt-2-hmt-language-model-validation-8032a50ebc`
Run ID: `parameter-matched-mini-gpt-2-hmt-language-model-validation-8032a50ebc-20260524T102240224648+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Hierarchical memory tokens for 4k local GPT-2 training: enoch://control-plane/projects/hierarchical-memory-tokens-for-4k-local-gpt-2-training-7da2b07de8b1/runs/hierarchical-memory-tokens-for-4k-local-gpt-2-training-7da2b07de8b1-20260524T080336170772+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/868b1785ee47

## What looked useful

HMT-style recurrent memory trained successfully and consistently reduced validation loss versus a near-parameter-matched mini GPT baseline: mean long-window delta -0.2111 nats and mean short-window delta -0.1823 nats over three seeds, with HMT using 0.785% fewer parameters.

## Boundaries and scale limits

Character-level Tiny Shakespeare only; compact local HMT approximation; hundreds of training steps rather than convergence; three seeds; not GPT-2 BPE, WebText/OpenWebText, WikiText-103, or GPT-2-small-class scale.

## Claim scope

Small direct character-level language-model validation on Tiny Shakespeare: a compact segment-recurrent HMT-style LM with 637,280 parameters outperformed a 642,320-parameter mini GPT baseline after 800 steps across three seeds on 256-token validation windows.

## Why it stopped

Tier-1 direct small test produced a useful positive mechanism signal, but evidence remains toy-scale and insufficient for paper readiness.

## Recommended next action

Run a bounded deepen validation using GPT-2 BPE tokenization on WikiText-103 or OpenWebText-small with an exact HMT reproduction, matched GPT context controls, and memory-size/segment-length ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE-tokenized WikiText HMT vs parameter-matched mini-GPT confirmation
- Success threshold: HMT mean validation loss at least 0.05 nats lower than the strongest matched GPT control on multi-segment validation windows across at least three seeds, with no worse than 0.02 nats regression on single-segment windows.
- Stop condition: Stop if HMT fails to beat the strongest matched GPT control by 0.02 nats on multi-segment validation after stable training curves, or if the gain disappears under memory/segment ablation controls.

## Evidence references

- Artifact root: `<local-path>/projects/parameter-matched-mini-gpt-2-hmt-language-model-validation-8032a50ebc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
