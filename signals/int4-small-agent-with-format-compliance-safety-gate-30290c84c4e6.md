# INT4 Small Agent with Format-Compliance Safety Gate

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int4-small-agent-with-format-compliance-safety-gate-30290c84c4e6`
Run ID: `int4-small-agent-with-format-compliance-safety-gate-30290c84c4e6-20260628T070734814443+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b49dbf04196f

## What looked useful

JSON parsability alone was unsafe: fake_int4 produced parseable JSON on 21/24 tasks but 12/24 were semantically wrong. The gate accepted only 9/24 correct fake_int4 actions and rejected all wrong/invalid actions; dense had 5/24 parseable-but-wrong actions also rejected by the gate.

## Boundaries and scale limits

Fake INT4 used symmetric 4-bit weight rounding followed by dequantized inference, not a production INT4 kernel. The task set was small, non-adversarial arithmetic, not real multi-step agent operation or side-effecting tool use.

## Claim scope

On 24 local arithmetic JSON tool-call prompts with Qwen2.5-0.5B-Instruct, a strict schema-and-semantic gate rejected parseable but wrong dense and fake-INT4 outputs with zero unsafe accepts.

## Why it stopped

No-paper useful signal: bounded proxy supports the safety-gate mechanism, but it is not full validation because INT4 runtime behavior and broader agent tasks were only proxied.

## Recommended next action

Run a bounded deepen follow-up using a true INT4 runtime plus adversarial JSON/tool-use prompts, measuring parseable-but-wrong rate, gate false rejects, and unsafe accepts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True INT4 Structured-Agent Gate Benchmark
- Success threshold: Strict semantic gate has zero unsafe accepts and at least 90% of the correct-action acceptance rate of the best non-gated baseline while reducing parseable-but-wrong accepted actions by at least 95%.
- Stop condition: Stop if true INT4 runtime cannot load locally after ordinary installation attempts, or if unsafe gate accepts exceed 1% on the benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/int4-small-agent-with-format-compliance-safety-gate-30290c84c4e6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
