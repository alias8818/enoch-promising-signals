# CPU N-Gram Speculative Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-draft-c8e3ad31f021`
Run ID: `cpu-n-gram-speculative-draft-c8e3ad31f021-20260530T030031424772+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/22735ade539b

## What looked useful

Single-thread Python n-gram lookup was fast enough for proposer overhead not to dominate. Best ideal verifier speedups were only 1.032x-1.088x on prose, 1.294x-1.469x on small code/readme samples, 2.011x on mixed templates, and 8.000x on a repetitive synthetic control.

## Boundaries and scale limits

No production BPE tokenizer, no real transformer verifier, no GPU end-to-end decoding loop, no latency batching model, and only small public corpora/synthetic controls. Ideal verifier speedup is an upper-bound proxy, not measured deployed tokens/sec.

## Claim scope

Bounded proxy simulation of a CPU longest-suffix n-gram speculative decoding proposer over regex-tokenized public text/code streams. The mechanism is CPU-cheap and can materially reduce oracle verifier calls on repetitive, templated, and code-like streams, but shows weak utility on ordinary prose.

## Why it stopped

Proxy evidence is mixed: early falsification of broad generic-prose usefulness for a simple CPU n-gram proposer, with a positive bounded signal only on repeated/code-like streams; not a full validation.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next test is an end-to-end small-LLM speculative decoding integration on BPE-tokenized code/template/prose prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end BPE CPU n-gram speculative decoding on a small local LLM
- Success threshold: At least 1.15x measured end-to-end tokens/sec on code/template-heavy prompts, no more than 5% throughput loss on prose, and accepted-token statistics consistent across at least three prompt families.
- Stop condition: Stop if BPE-tokenized acceptance on code/template prompts is below 10% or measured end-to-end throughput is not at least 1.05x after a smoke implementation, because the proxy signal is then not translating.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-draft-c8e3ad31f021`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
